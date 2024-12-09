import datetime
import random

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.abs_repo import Repository
from app.domain.models import ClientVersionORM
from app.domain.schemas import ClientVersion
import faker


class AsyncRepository(Repository):

    async def check_version(
        self,
        name: str,
        version: float | str,
        session: AsyncSession,
    ) -> list[ClientVersion]:
        query = select(ClientVersionORM).where(
            ClientVersionORM.name == name,
            ClientVersionORM.version > float(version),
        )
        async with session.begin():
            result = await session.execute(query)
            check_versions = result.scalars().all()
            return [ClientVersion.model_validate(item) for item in check_versions]

    async def add_some_versions(self, session: AsyncSession):
        names = [
            "cfps-prod",
            "cfps-stage",
            "cfps-dev",
        ]
        bools = [
            True,
            False
        ]

        versions = [
            ClientVersionORM(
                name=faker.Faker().random_element(names),
                version=faker.Faker().random_int(min=1, max=100) + 0.5,
                date=datetime.datetime.now().date(),
                force_update=faker.Faker().random_element(bools),
                changelog="".join(faker.Faker().word() for _ in range(20))
                ,
            )
            for _ in range(30)
        ]
        session.add_all(versions)
        await session.commit()
        return names

    async def get_unique_names(self):
        ...