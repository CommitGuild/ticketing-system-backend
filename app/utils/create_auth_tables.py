import asyncio
from app.db.auth import engine
from app.models.auth import User, OAuthAccount  # imports trigger metadata

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(create_tables())