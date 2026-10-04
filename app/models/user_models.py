from app.db.database import BASE
from sqlalchemy import Column, String, text, TIMESTAMP, Enum, Boolean
from app.core.enums import UserRole
import uuid


class UserModel(BASE):
    __tablename__ = "users"

    id = Column(String, primary_key=True, nullable=False, default=str(uuid.uuid4()))

    name = Column(String, nullable=False)

    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, unique=False, nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)

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
