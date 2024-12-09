from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class SyncDatabaseConfig(BaseSettings):
    """Configuration for the sync database."""

    model_config = SettingsConfigDict(
        env_file="../../.env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_prefix="POSTGRES_",
    )

    user: str
    password: str
    host: str
    port: str
    name: str = Field(validation_alias="postgres_db")

    database_type: str = Field(default="postgresql")
    driver: str = Field(default="psycopg2")

    @property
    def url(self) -> str:
        """Concatenate .env db-params to url."""
        db_url = f"{self.database_type}+{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
        return db_url


sync_database_config = SyncDatabaseConfig()
