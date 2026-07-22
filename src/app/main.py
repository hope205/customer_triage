from fastapi import FastAPI
from sqlalchemy import engine
from src.app.core.database import engine, Base
from app.models import business
from src.app.api.routes import router



app = FastAPI()

Base.metadata.create_all(
    bind=engine
)



app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Inventory AI Agent API running"
    }

    