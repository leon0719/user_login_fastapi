from sqlalchemy.orm import sessionmaker
from config import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from models import User
from models import Base


SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{settings.database_username}:{settings.database_password}"
)
SQLALCHEMY_DATABASE_URL2 = (
    f"@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
)


SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL + SQLALCHEMY_DATABASE_URL2
# Base = declarative_base()

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

async_Session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session():
    async with async_Session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session=session, user_table=User)
