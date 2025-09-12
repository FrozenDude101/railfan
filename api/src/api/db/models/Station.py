from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import StationNode

from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class StationBase(SQLModel):
    name: str

class Station(StationBase, table = True):
    id: UUID = Field(primary_key = True, default_factory = uuid4)

    nodes: list["StationNode"] = Relationship(back_populates = "station")
