from database import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import String, TIMESTAMP, text
from fastapi_users.db import SQLAlchemyBaseUserTableUUID


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    phone_number = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
