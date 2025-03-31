from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class CompanyBase(BaseModel):
    company_name: Optional[str] = Field(max_length=50)
    company_address: Optional[str] = Field(max_length=100)
    company_email: Optional[EmailStr] = None
    company_phone: Optional[str] = Field(max_length=30)

    user1: Optional[str] = Field(max_length=50)
    user2: Optional[str] = Field(max_length=50)
    user3: Optional[str] = Field(max_length=50)

    class Config:
        from_attributes = True


class CompanyCreate(CompanyBase):
    company_name: str = Field(..., max_length=50)
    company_email: EmailStr


class CompanyUpdate(CompanyBase):
    ...


class CompanyOut(CompanyBase):
    company_id: str
    company_name: str = Field(..., max_length=50)
    company_email: EmailStr