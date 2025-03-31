from fastapi import FastAPI
from app.api.routes import companies_router

app = FastAPI(title="Async Company CRUD with FastAPI and PostgreSQL")

app.include_router(companies_router, prefix="/companies", tags=["Companies"])