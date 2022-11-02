from fastapi import HTTPException
from numpy import record
from sqlalchemy.orm import Session
from sql.models import models
from sql.dtos import schemas

def create_record_audio(db: Session, audio:schemas.AudioGenerated):
    db_audio = models.ManageAudioGenerated(**audio.dict())
    db.add(db_audio)
    db.commit()
    db.refresh(db_audio)
    return db_audio



def delete_record_audio(db:Session,id:int):
    recordAudio=db.get(models.ManageAudioGenerated,id)
    db.delete(recordAudio)
    db.commit()
    return {"ok": True}

def get_all_record_audio(db:Session):
         return db.query(models.ManageAudioGenerated).all()

def upadte_record(db:Session,id:int,updateRecord:schemas.UpdateAudioGenerated):
        record_audio=db.get(models.ManageAudioGenerated,id)
        if not record_audio:
            raise HTTPException(status_code=404, detail="Record not found")
        hero_data =updateRecord.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(record_audio, key, value)
        db.add(record_audio)
        db.commit()
        db.refresh(record_audio)
        return db.get(models.ManageAudioGenerated,id)


