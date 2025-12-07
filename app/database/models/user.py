from typing import List
from uuid import UUID

from sqlalchemy import UUID as SQLUUID
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .contract import Contract
from .role import Role


class User(Base):
    __tablename__: str = "user"

    id: Mapped[UUID] = mapped_column(
        SQLUUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    name: Mapped[str] = mapped_column()
    lastname: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(index=True, unique=True)
    password: Mapped[str] = mapped_column()
    id_role: Mapped[int] = mapped_column(ForeignKey("role.id"))
    external_reference: Mapped[int] = mapped_column(unique=True, nullable=True)

    role: Mapped[Role] = relationship()
    contract: Mapped[List[Contract]] = relationship(
        secondary="user_x_contract",
        primaryjoin="User.id == UserContract.referer_id_user",
        secondaryjoin="UserContract.contract_id == Contract.id",
        viewonly=True,
    )

    def activate(self) -> None:
        self.is_active = True

    def set_external_refence(self, external_reference: int) -> None:
        self.external_reference = external_reference
