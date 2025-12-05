from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TicketTypeBase(BaseModel):
    name: str
    description: Optional[str] = None


class TicketTypeCreate(TicketTypeBase):
    pass  # same fields as base, no id


class TicketTypeRead(TicketTypeBase):
    id: int
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True  # important for Prisma -> Pydantic
