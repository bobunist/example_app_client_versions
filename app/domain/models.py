from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, String, Text, func, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class MyBase(DeclarativeBase):
    """Base model."""
    pass


class BaseModel(MyBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class ClientVersionORM(BaseModel):
    __tablename__ = "client_versions"

    name: Mapped[str | None] = mapped_column(String, nullable=True)
    version: Mapped[float] = mapped_column(Float, nullable=False)
    date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        server_default=func.now(),
    )
    force_update: Mapped[bool] = mapped_column(Boolean, default=False)
    changelog: Mapped[str] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"Version=={self.version})"
