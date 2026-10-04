from app.db.database import BASE
from sqlalchemy import Column, String, TIMESTAMP, text, ForeignKey, Boolean

import uuid


class TeamsModels(BASE):
    __tablename__ = "teams"

    id = Column(
        String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4())
    )

    name = Column(String, nullable=False)

    org_id = Column(String, ForeignKey("organisation.id"), nullable=False)

    created_by = Column(String, ForeignKey("users.id"), nullable=False)

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )


class TeamMembersModel(BASE):
    __tablename__ = "team_members"

    id = Column(
        String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4())
    )

    team_id = Column(String, ForeignKey("teams.id"), nullable=False)

    org_id = Column(String, ForeignKey("organisation.id"), nullable=False)

    user_id = Column(String, ForeignKey("users.id"), nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)

    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )
