from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import Operator, RouteStation, RouteLeg

from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class Route(SQLModel, table = True):
    id: UUID = Field(primary_key = True, default_factory = uuid4)
    name: str

    operatorId: UUID = Field(foreign_key = "operator.id")
    operator: "Operator" = Relationship(back_populates = "routes")

    stations: list["RouteStation"] = Relationship(back_populates = "route")
    legs: list["RouteLeg"] = Relationship(back_populates = "route")
