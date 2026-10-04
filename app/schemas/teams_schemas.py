from pydantic import BaseModel, ConfigDict
from datetime import datetime


class TeamsReq(BaseModel):
    name: str
    org_id: str
    created_by: str


class TeamsRes(BaseModel):
    id: str
    name: str
    org_id: str
    created_by: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TeamMemberReq(BaseModel):
    org_id: str
    team_id: str
    user_id: str


class TeamMemberRes(BaseModel):
    # org_name: str
    user_id: str
    message: str
    # team_name: str

    model_config = ConfigDict(from_attributes=True)

class TeamDeleteMember(BaseModel):
    team_id: str
    user_id: str