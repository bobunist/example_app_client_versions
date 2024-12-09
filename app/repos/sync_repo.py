from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.abs_repo import Repository
from app.domain.models import ClientVersionORM
from app.domain.schemas import ClientVersion


class SyncRepository(Repository):

    def check_version(self, name: str, version: float | str, session: Session) -> list[ClientVersion]:
        query = select(ClientVersionORM).where(
            ClientVersionORM.name == name,
            ClientVersionORM.version > float(version),
        )

        result = session.execute(query)
        check_versions = result.scalars().all()
        session.commit()
        return [ClientVersion.model_validate(item) for item in check_versions]
