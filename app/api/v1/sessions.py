from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.database import get_session
from app.models.user_session import UserSession
from app.schemas.session import SessionCreate, SessionResponse, SessionUpdate
from uuid import UUID


router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.post("", response_model=SessionResponse)
async def create_session(
   session:SessionCreate,
   db:Session=Depends(get_session)
):
    new_session = UserSession(user_id=session.user_id)
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session


@router.get("/{session_id}", response_model=SessionResponse)
async def get_session(
    session_id:UUID,
    db:Session= Depends(get_session)
):
    session = db.query(UserSession).filter(UserSession.id ==session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session


@router.patch("/{session_id}", response_model=SessionResponse)
async def update_session(
    session_id: UUID,
    session_update: SessionUpdate,
    db: Session = Depends(get_session)
):
    session = db.query(UserSession).filter(UserSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session.ended_at = session_update.ended_at
    db.add(session)
    db.commit()
    db.refresh(session)
    return session
