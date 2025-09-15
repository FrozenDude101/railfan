from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import StationNode

from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class Station(SQLModel, table = True):
    id: UUID = Field(primary_key = True, default_factory = uuid4)
    name: str

    nodes: list["StationNode"] = Relationship(back_populates = "station")
