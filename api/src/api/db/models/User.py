from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.db.models import UserJourney

from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class User(SQLModel, table = True):
    id: UUID = Field(primary_key = True, default_factory = uuid4)
    displayName: str

    journeys: list["UserJourney"] = Relationship(back_populates = "user")
