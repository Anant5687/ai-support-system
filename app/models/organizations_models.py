from app.db.database import BASE
from sqlalchemy import Column, String, TIMESTAMP, text, Boolean
import uuid


class OrganisationModel(BASE):
    __tablename__ = "organisation"

    id = Column(String, nullable=False, primary_key=True, default=str(uuid.uuid4()))

    org_name = Column(String, nullable=False)

    org_desc = Column(String, nullable=True)

    is_active = Column(Boolean, nullable=False, default=True)

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )
