from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import OsmNode

from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class StationBase(SQLModel):
    name: str

class Station(StationBase, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)

    osmNodes: list["OsmNode"] = Relationship(back_populates="station")
