from fastapi import APIRouter, HTTPException
from fastapi import Depends

from sql.database import SessionLocal
from sqlalchemy.orm import Session
from sql.dtos import schemas
from sql.services.users import userservice 
router = APIRouter( 
    prefix="/api/users",
    tags=["UsersController"],
    responses={404: {"description": "Not found"}},
)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create_user(account : schemas.CreateAccountDto,db: Session = Depends(get_db)):
    checkExistedUser=userservice.get_user_by_username(db,account.username)
    if checkExistedUser:
        raise HTTPException(status_code=400, detail="Email already registered")
    newUser=userservice.create_user(db,account)
    return newUser