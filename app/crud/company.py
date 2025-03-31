from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from typing import Optional

from app.models import Company
from app.schemas import CompanyCreate, CompanyUpdate, CompanyOut
from app.exceptions import (
    EmailAlreadyExistsError,
    CompanyNotFoundError
)


async def get_company(db: AsyncSession, company_id: str) -> Optional[CompanyOut]:
    """Отримати компанію за id"""
    result = await db.execute(select(Company).where(Company.company_id == company_id))
    company = result.scalar_one_or_none()
    if not company:
        return None
    return CompanyOut.model_validate(company)

async def get_company_by_email(db: AsyncSession, company_email: str) -> Optional[CompanyOut]:
    """Отримати компанію за email"""
    result = await db.execute(select(Company).where(Company.company_email == company_email))
    company = result.scalar_one_or_none()
    if not company:
        return None
    return CompanyOut.model_validate(company)

async def create_company(db: AsyncSession, company_in: CompanyCreate) -> CompanyOut:
    """Створити компанію"""
    existing_company = await get_company_by_email(db, str(company_in.company_email))
    if existing_company:
        raise EmailAlreadyExistsError(f"Email {company_in.company_email} вже зайнятий")

    new_company = Company(**company_in.model_dump())

    db.add(new_company)
    await db.commit()
    await db.refresh(new_company)

    return CompanyOut.model_validate(new_company)


async def update_company(
        db: AsyncSession,
        company_id: str,
        company_in: CompanyUpdate
) -> CompanyOut:
    """Оновити компанію за id"""
    update_data = company_in.model_dump(exclude_unset=True)

    # Перевірити, чи зайнятий email
    if "company_email" in update_data:
        existing_company = await get_company_by_email(db, str(update_data["company_email"]))
        if existing_company and existing_company.company_id != company_id:
            raise EmailAlreadyExistsError(f"Email {update_data['company_email']} вже зайнятий")

    statement = (
        update(Company)
        .where(Company.company_id == company_id)
        .values(**update_data)
        .execution_options(synchronize_session="fetch")
    )

    result = await db.execute(statement)
    await db.commit()

    if result.rowcount == 0:
        raise CompanyNotFoundError(f"Компанія {company_id} не знайдена")

    return await get_company(db, company_id)


async def delete_company(db: AsyncSession, company_id: str) -> None:
    """Видалити компанію"""
    result = await db.execute(select(Company).where(Company.company_id == company_id))
    company = result.scalar_one_or_none()

    if not company:
        raise CompanyNotFoundError(f"Компанія {company_id} не знайдена")
    await db.delete(company)
    await db.commit()