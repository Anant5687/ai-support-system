from app.schemas.tickets_schemas import TicketReassignReq, TicketReq
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.teams_models import TeamsModels
from app.models.ticket_model import TicketModel
from app.models.user_models import UserModel


class TicketService:

    def __check_team__(team_id: str, db: Session):
        team = db.query(TeamsModels).filter(TeamsModels.id == team_id).first()

        if not team:
            raise HTTPException(
                status_code=404, detail=f"Team not found with {team_id}"
            )

    def __check_user__(user_id: str, db: Session):
        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=404, detail=f"User not found with {user_id}"
            )

    def __check_ticket__(ticket_id: str, db: Session):
        ticket = db.query(TicketModel).filter(TicketModel.id == ticket_id).first()

        if not ticket:
            raise HTTPException(
                status_code=404, detail=f"Ticket not found with {ticket_id}"
            )

        return ticket

    def get_all_ticket(db: Session):
        tickets = db.query(TicketModel).filter(TicketModel.is_active).all()

        return tickets

    def create_ticket(data: TicketReq, db: Session):
        TicketService.__check_team__(data.team_id, db)
        TicketService.__check_user__(data.created_by, db)
        assignee_id = data.assignee_id
        if assignee_id is None:
            assignee_id = data.created_by
        else:
            TicketService.__check_user__(assignee_id, db)

        new_ticket = TicketModel(
            **data.model_dump(exclude={"assignee_id"}),
            assignee_id=assignee_id,
        )

        db.add(new_ticket)
        db.commit()
        db.refresh(new_ticket)

        return new_ticket

    @staticmethod
    def reassign_ticket(ticket_id: str, data: TicketReassignReq, db: Session):
        ticket = TicketService.__check_ticket__(ticket_id, db)
        TicketService.__check_user__(data.assignee_id, db)

        ticket.assignee_id = data.assignee_id

        db.commit()
        db.refresh(ticket)

        return ticket

    def close_ticket(ticket_id: str, db: Session):
        ticket = TicketService.__check_ticket__(ticket_id, db)

        ticket.is_active = False
        db.commit()
        db.refresh(ticket)
        return ticket

    def reopen_ticket(ticket_id: str, db: Session):
        ticket = TicketService.__check_ticket__(ticket_id, db)

        ticket.is_active = True
        db.commit()
        db.refresh(ticket)
        return ticket

    def delete_ticket(ticket_id: str, db: Session):
        ticket = TicketService.__check_ticket__(ticket_id, db)

        db.delete(ticket)
        db.commit()

        return ticket
