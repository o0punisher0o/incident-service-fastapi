from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class IncidentBase(BaseModel):
    description: str
    status: Optional[str] = "open"
    source: Optional[str] = "operator"


class IncidentCreate(IncidentBase):
    pass


class IncidentUpdate(BaseModel):
    status: str


class Incident(IncidentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

