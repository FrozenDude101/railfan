from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import Station

from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class StationNode(SQLModel, table = True):
    id: UUID = Field(primary_key = True, default_factory = uuid4)
    osmNodeId: int

    stationId: UUID = Field(foreign_key = "station.id")
    station: "Station" = Relationship(back_populates = "nodes")
