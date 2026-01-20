from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import uuid4, UUID


class DetectedMisconception(SQLModel, table=True):
    id:UUID = Field(default_factory=uuid4, primary_key=True)
    session_id:UUID = Field(foreign_key="usersession.id")
    concept_id:str
    misconception:str
    confidence_level:str
    detected_at:datetime=Field(default_factory=datetime.utcnow)
