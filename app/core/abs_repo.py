from abc import ABC, abstractmethod
from typing import Any

from app.domain.schemas import ClientVersion


class Repository(ABC):

    @abstractmethod
    def check_version(self, name: str, version: float | str, session: Any) -> list[ClientVersion]:
        pass
