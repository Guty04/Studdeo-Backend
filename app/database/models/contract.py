from datetime import datetime
from uuid import UUID

from sqlalchemy import TIMESTAMP, func
from sqlalchemy import UUID as SQLUUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Contract(Base):
    __tablename__: str = "contract"

    id: Mapped[UUID] = mapped_column(
        SQLUUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    percentaje: Mapped[float] = mapped_column(nullable=False)
    valid_from: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False, default=func.now()
    )
    valid_to: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
