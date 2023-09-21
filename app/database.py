from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{settings.database_username}:{settings.database_password}"
)
SQLALCHEMY_DATABASE_URL2 = (
    f"@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
)


SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL + SQLALCHEMY_DATABASE_URL2

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

async_Session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
