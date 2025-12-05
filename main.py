# from contextlib import asynccontextmanager

# import fastapi
# from prisma import Prisma

# from app.database import db
# from app.schemas import TicketType


# @asynccontextmanager
# async def lifespan(app: fastapi.FastAPI):
#     await db.connect()
#     yield
#     await db.disconnect()


# app = fastapi.FastAPI(lifespan=lifespan)


# @app.post("/ticket-types")
# async def create_ticket_type(
#     ticket_type: TicketType,
#     db_conn: Prisma = fastapi.Depends(db.get_db),
# ):
#     await db_conn.tickettype.create(data=ticket_type.model_dump())
#     return {"message": "Ticket type created successfully"}

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.dependencies import db
from app.routers import ticket_type as ticket_type_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()


app = FastAPI(title="My Awesome API", lifespan=lifespan)

app.include_router(
    ticket_type_router.router,
    prefix="/ticket-types",
    tags=["ticket-types"],
)


# Optional: health check
@app.get("/health")
async def health():
    return {"status": "ok"}
