from fastapi import FastAPI
import uvicorn
from routes.gift import route as gift

app = FastAPI()

app.include_router(gift)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True)
# await create_tables()