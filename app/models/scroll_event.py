from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import uuid4, UUID



class ScrollEvent(SQLModel, table=True):
    id:UUID = Field(default_factory=uuid4, primary_key=True)
    page_view_id:UUID =  Field(foreign_key="pageview.id")
    scroll_position:float
    direction:str
    timestamp:datetime = Field(default_factory=datetime.utcnow)
