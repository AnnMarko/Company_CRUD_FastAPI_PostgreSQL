from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.schemas import CompanyCreate, CompanyUpdate, CompanyOut
from app.crud import company as company_crud
from app.exceptions import (
    EmailAlreadyExistsError,
    CompanyNotFoundError
)

router = APIRouter()

@router.post("", response_model=CompanyOut)
async def create_company_endpoint(
    company_in: CompanyCreate,
    db: AsyncSession = Depends(get_db)
) -> CompanyOut:
    """Створити компанію"""
    try:
        company = await company_crud.create_company(db, company_in)
    except EmailAlreadyExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    return company

@router.get("/{company_id}", response_model=CompanyOut)
async def get_company_endpoint(
    company_id: str,
    db: AsyncSession = Depends(get_db)
) -> CompanyOut:
    """Отримати компанію за id"""
    company = await company_crud.get_company(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Компанія не знайдена")
    return company

@router.patch("/{company_id}", response_model=CompanyOut)
async def update_company_endpoint(
    company_id: str,
    company_in: CompanyUpdate,
    db: AsyncSession = Depends(get_db)
) -> CompanyOut:
    """Оновити компанію за id"""
    try:
        company = await company_crud.update_company(db, company_id, company_in)
    except CompanyNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except EmailAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return company

@router.delete("/{company_id}")
async def delete_company_endpoint(
    company_id: str,
    db: AsyncSession = Depends(get_db)
) -> dict:
    """Видалити компанію"""
    try:
        await company_crud.delete_company(db, company_id)
    except CompanyNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return {"msg": f"Компанія {company_id} видалена"}