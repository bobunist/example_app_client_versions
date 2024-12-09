from datetime import datetime

from pydantic import ConfigDict, BaseModel


class ClientVersion(BaseModel):
    id: int
    name: str | None = None
    version: float
    force_update: bool
    date: datetime
    changelog: str

    model_config = ConfigDict(from_attributes=True)
