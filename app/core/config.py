from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="Company_CRUD_FastAPI_PostgreSQL/.env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore"
    )

    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost:5432/my_db"

    @classmethod
    def load(cls) -> "Config":
        return cls()


configuration = Config()