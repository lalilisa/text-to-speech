
from sqlalchemy.orm import Session
from sql.models import models
from sql.dtos import schemas

def create_user(db: Session, user: schemas.CreateAccountDto):
    db_user = models.Account(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username:str):
       return db.query(models.Account).filter(models.Account.username == username).first()