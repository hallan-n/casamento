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

async def wait_for_db(retries=10, delay=2):
    for i in range(retries):
        try:            
            await create_tables()
            return
        except Exception as e:
            print(f"🔁 Tentativa {i + 1}/{retries} falhou: {e}")
            await asyncio.sleep(delay)
    raise RuntimeError("❌ Falha ao conectar ao banco de dados.")


async def setup():
    await wait_for_db()


if __name__ == "__main__":
    asyncio.run(setup())
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
