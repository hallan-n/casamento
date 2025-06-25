import asyncio

import uvicorn
from database import create_tables
from fastapi import FastAPI
from routes.auth import route as auth
from routes.gift import route as gift
from routes.guest import route as guest
from web.start import init

app = FastAPI()

app.include_router(guest)
app.include_router(gift)
app.include_router(auth)
init(app)


async def setup():
    await create_tables()


if __name__ == "__main__":
    asyncio.run(create_tables())
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
