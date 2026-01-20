from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import UUID, uuid4   


class  UserSession(SQLModel, table=True):
    id:UUID =Field(default_factory=uuid4, primary_key=True)
    user_id:str =Field(index=True)
    started_at:datetime =Field(default_factory=datetime.utcnow)
    ended_at:datetime |  None =None
