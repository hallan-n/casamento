from database import Connection, Gift, Guest
from sqlmodel import select


async def create(data: Gift | Guest):
    async with Connection() as conn:
        conn.add(data)
        await conn.commit()
        await conn.refresh(data)
        return data


async def read(Schema: Gift | Guest, id: int | str = None) -> Gift | Guest:
    async with Connection() as conn:
        if id:
            return await conn.get(Schema, id)
        stmt = select(Schema)

        if Schema == Gift:
            stmt = stmt.order_by(Schema.price)
            
        result = await conn.execute(stmt)
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
