from abc import ABC, abstractmethod
from typing import Any


class DatabaseClient(ABC):
    """Abs client for the database."""

    @abstractmethod
    async def get_session(self) -> Any:
        """Get a session."""
        pass

    @abstractmethod
    async def connect(self) -> None:
        """Connect the client."""
        pass

    @abstractmethod
    async def disconnect(self) -> None:
        """Disconnect the client."""
        pass
