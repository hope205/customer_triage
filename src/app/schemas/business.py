from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, EmailStr
import uuid


class BusinessCreate(BaseModel):
    name: str
    slug: str
    email: EmailStr



class BusinessResponse(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    email: EmailStr
    is_active: bool
    created_at: datetime


    class Config:
        from_attributes = True


class BusinessUpdateRequest(BaseModel):
    """Business update request schema"""
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = Field(None, max_length=20)
   