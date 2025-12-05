from fastapi import APIRouter, Depends, HTTPException, status
from prisma import Prisma
from app.schemas.ticket_type import TicketTypeCreate, TicketTypeRead
from app.dependencies import get_db

router = APIRouter()


@router.post(
    "/",
    response_model=TicketTypeRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_ticket_type(
    ticket_type_in: TicketTypeCreate,
    db: Prisma = Depends(get_db),
):
    try:
        created = await db.tickettype.create(
            data=ticket_type_in.model_dump(exclude_unset=True)
        )
        return created
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{ticket_type_id}", response_model=TicketTypeRead)
async def get_ticket_type(ticket_type_id: int, db: Prisma = Depends(get_db)):
    ticket_type = await db.tickettype.find_unique(where={"id": ticket_type_id})
    if not ticket_type:
        raise HTTPException(status_code=404, detail="Ticket type not found")
    return ticket_type
