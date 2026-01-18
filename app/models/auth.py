from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi_users.db import (
    SQLAlchemyBaseUserTableUUID,
    SQLAlchemyBaseOAuthAccountTableUUID,
)


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID):
    pass


class User(SQLAlchemyBaseUserTableUUID):
    username: Mapped[Optional[str]] = mapped_column(
        String(50), unique=True, nullable=True
    )

    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        OAuthAccount, lazy="joined", cascade="all, delete-orphan"
    )
