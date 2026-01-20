from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import uuid4, UUID




class Intervention(SQLModel, table=True):
    id:UUID = Field(default_factory=uuid4, primary_key=True)
    misconception_id:UUID = Field(foreign_key="detectedmisconception.id")
    intervention_type:str
    prompt_shown:str
    user_response: str | None = None
    created_at:datetime = Field(default_factory=datetime.utcnow)
