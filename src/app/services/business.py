from sqlalchemy.orm import Session
from app.models import business
from src.app.schemas.business import BusinessCreate




def create_business(
    db: Session,
    business_data: BusinessCreate
):

    business = business.Business(
        name=business_data.name,
        slug=business_data.slug,
        email=business_data.email
    )

    db.add(business)
    db.commit()
    db.refresh(business)

    return business