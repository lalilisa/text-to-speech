from typing import List, Union

from pydantic import BaseModel

#DTO
class CreateAccountDto(BaseModel):
    username: str
    password:str


class AudioGenerated(BaseModel):
    inputText: str
    words: int
    isGenPath:bool
    outputPathAudio:str 


class UpdateAudioGenerated(BaseModel):

    inputText: str
    words: int
    isGenPath:bool
    outputPathAudio:str 



