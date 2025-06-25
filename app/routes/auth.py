from consts import ACCESS_TOKEN, PWD, USER
from dto import PostLogin
from fastapi import APIRouter, HTTPException

route = APIRouter(prefix="/auth", tags=["Auth", "Publico"])


@route.post("/")
async def auth(login: PostLogin):
    """Insere um presente"""
    if login.user == USER and login.password == PWD:
        return {
            "access_token": ACCESS_TOKEN,
        }
    raise HTTPException(401, "Login incorreto")
