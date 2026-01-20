from uuid import UUID

from fastapi import APIRouter

from httpx_oauth.clients.google import GoogleOAuth2
from fastapi_users import FastAPIUsers

from app.deps.auth import get_user_manager
from app.core.security import auth_backend
from app.config.settings import settings
from app.models.auth import User

fastapi_users = FastAPIUsers[User, UUID](
    get_user_manager,
    [auth_backend],
)

router = APIRouter(prefix="/auth", tags=["auth"])

# Google
if settings.GOOGLE_CLIENT_ID and settings.GOOGLE_CLIENT_SECRET:
    google_client = GoogleOAuth2(
        client_id=settings.GOOGLE_CLIENT_ID,
        client_secret=settings.GOOGLE_CLIENT_SECRET,
    )
    router.include_router(
        fastapi_users.get_oauth_router(
            google_client,
            auth_backend,
            settings.SECRET_KEY.get_secret_value(),
            associate_by_email=True,  # ← key for scaling: link by email
            is_verified_by_default=True,
            # redirect_url="http://localhost:3000/success"  # frontend after login
        ),
        prefix="/google",
    )
