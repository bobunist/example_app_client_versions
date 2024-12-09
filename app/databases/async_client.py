from singleton import Singleton
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config.async_database import async_database_config
from app.core.abs_client import DatabaseClient


class AsyncDatabaseClient(metaclass=Singleton):
    """Async client for the database."""

    _engine: AsyncEngine | None = None
    _session_maker: async_sessionmaker[AsyncSession] | None = None

    async def get_session(self) -> AsyncSession:
        """Get a session."""
        return self._session_maker()

    async def connect(self) -> None:
        """Connect the client."""
        if self._session_maker is None:
            self._engine = create_async_engine(
                async_database_config.url,
                pool_size=20,
                max_overflow=0,
            )
            self._session_maker = async_sessionmaker(
                self._engine,
            )

    async def disconnect(self) -> None:
        """Disconnect the client."""
        if self._engine is not None:
            await self._engine.dispose()
            self._engine = None
            self._session_maker = None
