from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.app.core.database import get_db
from src.app.schemas.business import BusinessCreate, BusinessResponse
from src.app.services.business import create_business



router = APIRouter()



@router.post(
    "/create_business",
    response_model=BusinessResponse
)
def create_new_business(business: BusinessCreate, db: Session = Depends(get_db)):

    return create_business(
        db,
        business
    )



@router.get("/health")
def health():

    return {
        "status": "API is healthy"
    }


