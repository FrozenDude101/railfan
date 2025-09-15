from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import LegPartialWay, LegWay

from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class Leg(SQLModel, table = True):
    id: UUID = Field(primary_key = True, default_factory = uuid4)
    name: str

    ways: list["LegWay"] = Relationship(back_populates = "leg")
    partialWays: list["LegPartialWay"] = Relationship(back_populates = "leg")
