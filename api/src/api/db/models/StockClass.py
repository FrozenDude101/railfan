from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import Stock

from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class StockClass(SQLModel, table = True):
    id: UUID = Field(primary_key = True, default_factory = uuid4)
    name: str

    stock: list["Stock"] = Relationship(back_populates = "stockClass")
