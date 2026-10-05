from pydantic import BaseModel, ConfigDict

from datetime import datetime


class TicketReq(BaseModel):
    name: str
    description: str
    created_by: str
    team_id: str
    assignee_id: str | None = None


class TicketReassignReq(BaseModel):
    assignee_id: str


class TicketRes(BaseModel):
    id: str
    name: str
    description: str
    created_by: str
    team_id: str
    assignee_id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
