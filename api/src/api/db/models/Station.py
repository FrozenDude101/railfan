from __future__ import annotations

from sqlmodel import SQLModel

class Station(SQLModel):
    osmNodes: list[int]
    name: str
