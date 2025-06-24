import asyncio

import uvicorn
from database import create_tables
from fastapi import FastAPI
from routes.gift import route as gift

app = FastAPI()

app.include_router(gift)


async def setup():
    await create_tables()


if __name__ == "__main__":
    asyncio.run(create_tables())
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
