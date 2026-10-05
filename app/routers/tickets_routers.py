from app.services.tickets_service import TicketService
from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.tickets_schemas import TicketReassignReq, TicketReq, TicketRes

from app.db.database import get_db

router = APIRouter(prefix="/ticket", tags=["Ticket"])


@router.get("/", response_model=list[TicketRes])
def get_all_tickets(db: Session = Depends(get_db)):
    try:
        TicketService.get_all_ticket(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.post("/create", response_model=TicketRes)
def create_ticket(data: TicketReq, db: Session = Depends(get_db)):
    try:
        TicketService.create_ticket(data, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.patch("/{ticket_id}/reassign", response_model=list[TicketRes])
def reassign_ticket(
    ticket_id: str, data: TicketReassignReq, db: Session = Depends(get_db)
):
    try:
        TicketService.reassign_ticket(ticket_id, data, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.patch("/{ticket_id}/close", response_model=list[TicketRes])
def close_ticket(ticket_id: str, db: Session = Depends(get_db)):
    try:
        TicketService.close_ticket(ticket_id, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.patch("/{ticket_id}/reopen", response_model=list[TicketRes])
def reopen_ticket(ticket_id: str, db: Session = Depends(get_db)):
    try:
        TicketService.reopen_ticket(ticket_id, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.delete("/{ticket_id}/delete", response_model=list[TicketRes])
def delete_ticket(ticket_id: str, db: Session = Depends(get_db)):
    try:
        TicketService.delete_ticket(ticket_id, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )
