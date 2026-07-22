from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import Base
import uuid

class Integration(Base):
    __tablename__ = "integrations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    platform = Column(String(255), nullable=False)
    access_token = Column(String(255), nullable=False, unique=True)
    store_url = Column(String(255),nullable=True)
    business_id = Column(UUID(as_uuid=True),ForeignKey("businesses.id"),nullable=False)


    business = relationship("Business", back_populates="integrations")