from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import Leg

from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class LegWay(SQLModel, table = True):
    id: UUID = Field(primary_key = True, default_factory = uuid4)
    osmWayId: int

    legId: UUID = Field(foreign_key = "leg.id")
    leg: "Leg" = Relationship(back_populates = "ways")
