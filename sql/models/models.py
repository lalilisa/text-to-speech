from enum import unique
from operator import index, length_hint
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


##Entity

class Account(Base):
    __tablename__="account"
    id = Column(Integer, primary_key=True, index=True)
    username=Column(String(255),unique=True,index=True)
    password=Column(String(255),unique=True,index=True)


class ManageAudioGenerated(Base):
    __tablename__="manager_audio_generated"
    id = Column(Integer, primary_key=True, index=True)
    hashcode=Column(String(255),unique=True,index=True)
    inputText=Column(String(255),unique=True,index=True)
    audioNameOutput=Column(String(255),unique=True,index=True)
    words=Column(Integer)
    isGenPath=Column(Boolean,default=True)
    outputPathAudio=Column(String(255),unique=True,index=True)




