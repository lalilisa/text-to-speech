from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#Connect databse
USERNAME="trimai"
PASSWORD="trimai"
DATABASE_NAME="base"
PORT="3306"
DATABASE_URL = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@db:{PORT}/{DATABASE_NAME}"

engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
