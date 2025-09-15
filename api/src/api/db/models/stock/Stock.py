from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import Operator, StockClass

from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class Stock(SQLModel, table = True):
    id: UUID = Field(primary_key = True, default_factory = uuid4)
    unitNumber: int

    stockClassId: UUID = Field(foreign_key = "stockclass.id")
    stockClass: "StockClass" = Relationship(back_populates = "stock")

    operatorId: UUID = Field(foreign_key = "operator.id")
    operator: "Operator" = Relationship(back_populates = "stock")
