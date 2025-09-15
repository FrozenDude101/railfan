from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import Stock, Route, Station, User

from sqlalchemy.orm import mapped_column
from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class UserJourney(SQLModel, table = True, foreign_keys = []):
    id: UUID = Field(primary_key = True, default_factory = uuid4)

    stockId: UUID = Field(foreign_key = "stock.id")
    stock: "Stock" = Relationship()

    routeId: UUID = Field(foreign_key = "route.id")
    route: "Route" = Relationship()

    fromStationId: UUID = Field(foreign_key = "station.id")
    fromStation: "Station" = Relationship(sa_relationship_kwargs = { "foreign_keys": "UserJourney.fromStationId" })

    toStationId: UUID = Field(foreign_key = "station.id")
    toStation: "Station" = Relationship(sa_relationship_kwargs = { "foreign_keys": "UserJourney.toStationId" })

    userId: UUID = Field(foreign_key = "user.id")
    user: "User" = Relationship(back_populates = "journeys")
