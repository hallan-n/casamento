import uuid
from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, Relationship, SQLModel


class Gift(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    thumb: str = Field(min_length=3, max_length=255, nullable=False)
    name: str = Field(min_length=3, max_length=255, nullable=False)
    url: str = Field(min_length=3, max_length=255, nullable=False)
    price: float = Field(nullable=False)

    guest_id: Optional[uuid.UUID] = Field(default=None, foreign_key="guest.id")
    guest: Optional["Guest"] = Relationship(back_populates="gifts")


class Guest(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(min_length=3, max_length=100, nullable=False)
    phone: str = Field(min_length=3, max_length=100, default="", nullable=False)
    is_confirmed: bool = Field(default=False)
    description: str = Field(min_length=3, max_length=100, default="")

    gifts: List[Gift] = Relationship(back_populates="guest")


DATABASE_URL = "mysql+aiomysql://neves:12qwaszx@localhost:3306/casamento"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Connection:
    def __init__(self):
        self.session = None

    async def __aenter__(self) -> AsyncSession:
        self.session = async_session()
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)