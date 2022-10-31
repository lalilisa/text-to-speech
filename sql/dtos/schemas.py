from typing import List, Union

from pydantic import BaseModel

#DTO
class CreateAccountDto(BaseModel):
    username: str
    password:str


class AudioGenerated(BaseModel):
    hashcode: str
    inputText: str
    audioNameOutput: str
    words: int
    isGenPath:bool
    outputPathAudio:str 


class UpdateAudioGenerated(BaseModel):
    hashcode: str
    inputText: str
    audioNameOutput: str
    words: int
    isGenPath:bool
    outputPathAudio:str 



