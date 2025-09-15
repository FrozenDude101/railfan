from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import Route, Station

from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class RouteStation(SQLModel, table = True):
    id: UUID = Field(primary_key = True, default_factory = uuid4)
    index: int

    routeId: UUID = Field(foreign_key = "route.id")
    route: "Route" = Relationship(back_populates = "stations")

    stationId: UUID = Field(foreign_key = "station.id")
    station: "Station" = Relationship()
