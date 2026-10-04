from pydantic import BaseModel, EmailStr, ConfigDict
from app.core.enums import UserRole
from datetime import datetime


class UserCreateReq(BaseModel):
    name: str
    role: UserRole
    email: EmailStr
    password: str


class UserCreateRes(BaseModel):
    name: str
    role: UserRole
    email: EmailStr
    id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class LoginReq(BaseModel):
    password: str
    email: EmailStr


class LoginRes(BaseModel):
    access_token: str
    role: UserRole
    id: str
    name: str
    token_type: str
    model_config = ConfigDict(from_attributes=True)
