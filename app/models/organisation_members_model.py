from app.db.database import BASE
from sqlalchemy import Column, String, text, TIMESTAMP, ForeignKey
import uuid


class OrgMemberModel(BASE):
    __tablename__ = "organisation_members"

    id = Column(String, nullable=False, primary_key=True, default=str(uuid.uuid4()))

    user_id = Column(String, ForeignKey("users.id"), nullable=False)

    org_id = Column(String, ForeignKey("organisation.id"), nullable=False)

    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )
