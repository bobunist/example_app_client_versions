from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.databases.async_client import AsyncDatabaseClient
from app.databases.sync_client import SyncDatabaseClient
from app.repos.async_repo import AsyncRepository
from app.repos.sync_repo import SyncRepository

AsyncSessionDep = Annotated[
    AsyncSession,
    Depends(AsyncDatabaseClient().get_session),
]

SyncSessionDep = Annotated[
    Session,
    Depends(SyncDatabaseClient().get_session),
]

SyncRepoDep = Annotated[
    SyncRepository,
    Depends()
]

AsyncRepoDep = Annotated[
    AsyncRepository,
    Depends()
]
