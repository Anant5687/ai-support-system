from pydantic import BaseModel, ConfigDict
from datetime import datetime


class OrganisationReq(BaseModel):
    org_name: str
    org_desc: str


class OrganisationMemberReq(BaseModel):
    user_id: str
    org_id: str


class OrganisationMemberRes(BaseModel):
    id: str
    user_id: str
    org_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class OrganisationRes(BaseModel):
    id: str
    org_name: str
    org_desc: str
    created_at: datetime
    members: list[OrganisationMemberRes] = []

    model_config = ConfigDict(from_attributes=True)
