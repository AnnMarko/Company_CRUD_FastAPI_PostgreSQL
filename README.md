# Company API

Цей проєкт реалізує API для створення компаній у системі моніторингу обслуговування транспортних засобів.

## 🔧 Стек технологій

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker + Docker Compose
- Alembic

## 📦 Поля компанії

| Поле             | Тип      | Обов'язкове  | Унікальне  |
|------------------|----------|--------------|------------|
| company_id       | рядок    | так          | так        |
| company_name     | рядок    | так          | ні         |
| company_address  | рядок    | ні           | ні         |
| company_email    | рядок    | так          | так        |
| company_phone    | рядок    | ні           | ні         |
| user1            | рядок    | ні           | ні         |
| user2            | рядок    | ні           | ні         |
| user3            | рядок    | ні           | ні         |

## 🚀 Як запустити проєкт

### 1. Клонувати репозиторій
`
git clone https://github.com/AnnMarko/Company_CRUD_FastAPI_PostgreSQL.git   
cd Company_CRUD_FastAPI_PostgreSQL
`
### 2. Створити .env файл
`
POSTGRES_USER=postgres   
POSTGRES_PASSWORD=postgres   
POSTGRES_DB=company_db   
POSTGRES_HOST=db   
POSTGRES_PORT=5432   
`
### 3. Запустити за допомогою Docker
`
docker-compose up --build
`

### 4. Запустити міграції
`
alembic revision --autogenerate -m 'message'
`

`
alembic upgrade head
`

### 5. Тестувати
`
http://localhost:8000/
`
