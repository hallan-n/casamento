from sqlmodel import select
from database import Gift, Guest, Connection


async def create(data: Gift | Guest):
    async with Connection() as conn:
        conn.add(data)
        await conn.commit()
        await conn.refresh(data)
        return data


async def read(Schema: Gift | Guest, id: int = None) -> Gift | Guest:
    async with Connection() as conn:
        if id:
            return await conn.get(Schema, id)
        result = await conn.execute(select(Schema))
        return result.scalars().all()

async def delete(data: Gift | Guest):
    async with Connection() as conn:
        await conn.delete(data)
        await conn.commit()
        return True

async def update(data: Gift | Guest):
    async with Connection() as conn:
        merged = await conn.merge(data)
        await conn.commit()
        await conn.refresh(merged)
        return merged
