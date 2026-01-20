from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import uuid4, UUID


class PageView(SQLModel, table =True):
    id:UUID = Field(default_factory=uuid4, primary_key=True )
    session_id:UUID = Field(foreign_key="usersession.id")
    page_url:str
    page_section:str
    time_spent_seconds:int = 0
    created_at:datetime = Field(default_factory=datetime.utcnow)
