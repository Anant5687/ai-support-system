from app.db.database import BASE
from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, text, Boolean
import uuid


class TicketModel(BASE):
    __tablename__ = "tickets"

    id = Column(String, nullable=False, primary_key=True, default=str(uuid.uuid4()))

    name = Column(String, nullable=False)

    decription = Column(String, nullable=True)

    created_by = Column(String, ForeignKey("users.id"), nullable=False)

    assignee_id = Column(
        String,
        ForeignKey("users.id"),
        nullable=False,
        default=lambda context: context.get_current_parameters()["created_by"],
    )

    team_id = Column(String, ForeignKey("teams.id"), nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    updated_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    )
