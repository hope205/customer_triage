import uuid
from sqlalchemy import Column,String,Numeric,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    business_id = Column(UUID(as_uuid=True),ForeignKey("businesses.id"),nullable=False)
    # ID from Shopify/Amazon/WooCommerce
    external_id = Column(String(255),nullable=False)
    name = Column(String(255),nullable=False)
    sku = Column(String(255),nullable=True)
    price = Column(Numeric(10,2),nullable=True)
    source = Column(String(50),nullable=False)


    business = relationship(
        "Business",
        back_populates="products"
    )

    inventory = relationship(
        "Inventory",
        back_populates="product",
        uselist=False
    )