from sqlmodel import Relationship, SQLModel, Field
import uuid
from typing import Optional, List



class Gift(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    thumb: str = Field(min_length=3, max_length=255, nullable=False)
    name: str = Field(min_length=3, max_length=255, nullable=False)
    url: str = Field(min_length=3, max_length=255, nullable=False)
    price: float = Field(nullable=False)

    guest_id: uuid.UUID = Field(foreign_key="guest.id", nullable=False)
    guest: Optional["Guest"] = Relationship(back_populates="gifts")


class Guest(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(min_length=3, max_length=100, nullable=False)
    phone: str = Field(min_length=3, max_length=100, default="", nullable=False)
    is_confirmed: bool = Field(default=False)
    description: str = Field(min_length=3, max_length=100, default="")

    gifts: List[Gift] = Relationship(back_populates="guest")