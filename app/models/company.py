from uuid import uuid4
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.db import Base


class Company(Base):
    __tablename__ = "companies"

    company_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4()), index=True, unique=True
    )
    company_name: Mapped[str] = mapped_column(String(50))
    company_address: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    company_email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    company_phone: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)

    user1: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    user2: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    user3: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)