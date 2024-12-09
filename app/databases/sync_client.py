from singleton import Singleton
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from app.config.sync_database import sync_database_config


class SyncDatabaseClient(metaclass=Singleton):
    """Sync client for the database."""

    _engine: Engine | None = None
    _session_maker: sessionmaker[Session] | None = None

    def get_session(self) -> Session:
        """Get a session."""
        return self._session_maker()

    def connect(self) -> None:
        """Connect the client."""
        if self._session_maker is None:
            self._engine = create_engine(
                sync_database_config.url,
                connect_args={"sslmode": "allow"},
                pool_size=50,
                max_overflow=100,
                pool_timeout=50,
                pool_recycle=3600,
                pool_pre_ping=True,
            )
            self._session_maker = sessionmaker(
                self._engine,
            )

    def disconnect(self) -> None:
        """Disconnect the client."""
        if self._engine is not None:
            self._engine.dispose()
            self._engine = None
            self._session_maker = None
