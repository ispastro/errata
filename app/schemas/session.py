from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class SessionCreate(BaseModel):
    user_id:str


class SessionResponse(BaseModel):
    id:UUID
    user_id:str
    started_at:datetime
    ended_at:datetime | None = None
