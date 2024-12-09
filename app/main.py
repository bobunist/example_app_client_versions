from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.databases.async_client import AsyncDatabaseClient
from app.databases.sync_client import SyncDatabaseClient
from app.deps import SyncSessionDep, SyncRepoDep, AsyncSessionDep, AsyncRepoDep
from starlette.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan of the application."""
    await AsyncDatabaseClient().connect()
    SyncDatabaseClient().connect()

    yield

    await AsyncDatabaseClient().disconnect()
    SyncDatabaseClient().disconnect()


app = FastAPI(
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)
app.add_middleware(GZipMiddleware)


@app.post("/")
async def add_versions(
    session: AsyncSessionDep,
    repo: AsyncRepoDep,
):
    return await repo.add_some_versions(
        session
    )


@app.get("/names")
async def get_names():
    pass


@app.get("/sync_in_sync/client/versions")
def sync_in_sync_client_versions(
    session: SyncSessionDep,
    repo: SyncRepoDep,
    name: str,
    version: float,
):
    return repo.check_version(
        name=name,
        version=version,
        session=session,
    )


@app.get("/sync_in_async/client/versions")
async def sync_in_async_client_versions(
    session: SyncSessionDep,
    repo: SyncRepoDep,
    name: str,
    version: float,
):
    return repo.check_version(
        name=name,
        version=version,
        session=session,
    )


@app.get("/right_sync_in_async/client/versions")
async def right_sync_in_async_client_versions(
    session: SyncSessionDep,
    repo: SyncRepoDep,
    name: str,
    version: float,
):
    return repo.check_version(
        name=name,
        version=version,
        session=session,
    )


@app.get("/async_in_async/client/versions")
async def async_in_async_client_versions(
    session: AsyncSessionDep,
    repo: AsyncRepoDep,
    name: str,
    version: float,
):
    return await repo.check_version(
        name=name,
        version=version,
        session=session,
    )
