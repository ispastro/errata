from fastapi  import FastAPI
from app.api.v1.health import router as health_router
from app.core.database import create_db_and_tables
from app.models.user_session import UserSession
app = FastAPI(title="Doct Tutur AI Backend API")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()




app.include_router(health_router)