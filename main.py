from email.mime import audio
import re
import unicodedata

from sqlalchemy.orm import Session

from vntts.hifigan.mel2wave import mel2wave
from vntts.nat.text2mel import text2mel
import numpy as np
import gradio as gr
import os
from starlette.responses import StreamingResponse
import soundfile as sf
import hashlib
from typing import Union
import uvicorn
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sql.services.manageaudio import manageaudioservice 

CUSTOM_PATH = "/gradio"

RESULT_PATH = "results"


def nat_normalize_text(text):
  """
  It removes all punctuation, replaces it with a silence token, and then normalizes the text

  :param text: The text to be normalized
  :return: The text is being normalized.
  """
  text = unicodedata.normalize("NFKC", text)
  text = text.lower().strip()
  sil = "sil"
  text = re.sub(r"[\n.,:]+", f" {sil} ", text)
  text = text.replace('"', " ")
  text = re.sub(r"\s+", " ", text)
  text = re.sub(r"[.,:;?!]+", f" {sil} ", text)
  text = re.sub("[ ]+", " ", text)
  text = re.sub(f"( {sil}+)+ ", f" {sil} ", text)
  return text.strip()

# get hash string from text input


def get_hash(text):
  return hashlib.md5(text.encode()).hexdigest()


def text_to_speech(text: str):
  if (text == ""):
    return None
  # prevent too long text
  if len(text) > 500:
    text = text[:500]
  text = nat_normalize_text(text)
  mel = text2mel(
      text,
      "lexicon.txt",
      0.2
  )
  print("mel shape", mel)
  wave = mel2wave(mel)
  return (wave * (2**15)).astype(np.int16)


def speak(text: str):
  text = nat_normalize_text(text)
  # check path if not exist, create new file
  if not os.path.exists(RESULT_PATH):
    os.makedirs(RESULT_PATH)
  # check file
  hash = get_hash(text)
  file_path = os.path.join(RESULT_PATH, hash + ".wav")
  # if os.path.exists(file_path):
  #   return file_path

  # make file
  file = open(file_path, "w+")
  file.close()
  y = text_to_speech(text)
  sf.write(file_path, y, 16000)
  return file_path

from sql.database import SessionLocal,engine
import sql.models.models as models
from router import apiuser
from sql.dtos import schemas
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router=apiuser.router)

class TextInput(BaseModel):
  text: str

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
  return {"Hello": "World"}
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/audio")
async def read_record(db: Session = Depends(get_db)):
  return manageaudioservice.get_all_record_audio(db)
@app.put("/audio/{id}")
async def udpate_record(id:int,updateRecord:schemas.UpdateAudioGenerated,db: Session = Depends(get_db)):
  return manageaudioservice.upadte_record(db,id,updateRecord)
@app.post("/audio")
async def save_record(body: TextInput,db: Session = Depends(get_db)):

    hashCode=get_hash(body.text)
    checkExistedRecord=manageaudioservice.get_record_by_hash_code(db,hashCode)
    audioName=hashCode+".wav"
    audioPath=os.path.join(RESULT_PATH, audioName)
    if checkExistedRecord is not None:
          if os.path.exists(audioPath):
            return {"file":audioName}
    audioByTTS=speak(body.text)
    numberWords=len(nat_normalize_text(body.text).split(" "))
    audioSchemas=schemas.AudioGenerated(hashcode=hashCode,inputText=body.text,audioNameOutput=audioName,words=numberWords,isGenPath=False,outputPathAudio=audioPath)
    #save to db
    print("-----------------------------------")
    manageaudioservice.create_record_audio(db,audioSchemas)
    # return path
    return {"file": audioByTTS}


@app.delete("/audio/{id}")
async def delete_record_audio(id:int,db:Session = Depends(get_db)):
    response=manageaudioservice.delete_record_audio(db,id)
    return response
# get audio from path
@app.get("/audio/{path}")
async def read_item(path: str):

  # check file
  if not os.path.exists(os.path.join(RESULT_PATH, path)):
    return {"error": "file not found"}

  return StreamingResponse(open(os.path.join(RESULT_PATH, path), "rb"), media_type="audio/wav")


title = "Chuyển văn bản thành giọng nói"

gr_io = gr.Interface(
    fn=speak,
    inputs="text",
    outputs="audio",
    title=title,
    examples=[],
    theme="default",
    allow_flagging="never",
)
gradio_app = gr.routes.App.create_app(gr_io)
app.mount(CUSTOM_PATH, gradio_app)

# if __name__ == "__main__":
#   uvicorn.run("main:app", port=5000, reload=True)
