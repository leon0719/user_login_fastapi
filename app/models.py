from sqlalchemy import Column
from sqlalchemy import String
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(SQLAlchemyBaseUserTableUUID, Base):
    username = Column(String(20))
