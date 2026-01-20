from uuid import UUID
from fastapi import Depends
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase  # ← this one!
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.auth import User, OAuthAccount
from app.db.auth import get_auth_session


class UserManager(UUIDIDMixin, BaseUserManager[User, UUID]):
    user_db_model = User
    # override if needed, e.g. on_after_oauth_register to sync with Prisma


async def get_user_db(session: AsyncSession = Depends(get_auth_session)):
    yield SQLAlchemyUserDatabase(session, User, OAuthAccount)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
