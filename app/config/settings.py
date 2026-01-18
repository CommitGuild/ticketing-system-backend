# app/config/settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # ignore unknown env vars
    )

    SECRET_KEY: SecretStr = Field(..., env="SECRET_KEY")
    DATABASE_URL: str = Field(
        ..., env="DATABASE_URL"
    )  # your postgres url for both Prisma & SQLAlchemy

    # OAuth providers (optional = None if not set)
    GOOGLE_CLIENT_ID: str | None = None
    GOOGLE_CLIENT_SECRET: str | None = None
    FACEBOOK_CLIENT_ID: str | None = None
    FACEBOOK_CLIENT_SECRET: str | None = None
    # add PATREON_, PAYPAL_ etc.

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 14  # 2 weeks default


# Instantiate here!
settings = Settings()
