from dataclasses import dataclass
from typing import List, Sequence

from app.database.models import Role
from app.repositories import RoleRepository
from app.schemas import RoleDB


@dataclass
class RoleService:
    repository: RoleRepository

    async def get_roles(self) -> List[RoleDB]:
        roles_db: Sequence[Role] = await self.repository.get_roles()

        return [RoleDB.model_validate(role) for role in roles_db]
