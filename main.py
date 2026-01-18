from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.deps.prisma import db
from app.routers import oauth, ticket_type as ticket_type_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()


app = FastAPI(title="Ticketing System Backend", lifespan=lifespan)

app.include_router(oauth.router)
app.include_router(
    ticket_type_router.router,
    prefix="/ticket-types",
    tags=["ticket-types"],
)


@app.get("/health")
async def health():
    return {"status": "ok"}
