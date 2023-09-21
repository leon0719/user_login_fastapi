from fastapi import Depends
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import (
    AuthenticationBackend,
    JWTStrategy,
    BearerTransport,
)
from fastapi_users.db import SQLAlchemyUserDatabase
from database import get_user_db
from config import settings

SECRET_KEY = settings.secret_key


class Usermanger(UUIDIDMixin, BaseUserManager):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield Usermanger(user_db)


cookie_transport = BearerTransport(tokenUrl="/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt", transport=cookie_transport, get_strategy=get_jwt_strategy
)

fastapi_users = FastAPIUsers(get_user_manager, [auth_backend])

active_user = fastapi_users.current_user(active=True)
