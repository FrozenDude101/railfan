from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import Station

from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID


class OsmNode(SQLModel, table=True):
    id: int = Field(primary_key=True)

    stationId: UUID = Field(foreign_key="station.id")
    station: "Station" = Relationship(back_populates="osmNodes")
