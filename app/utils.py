from consts import ACCESS_TOKEN
from fastapi import Header, HTTPException


def verify_token(token: str = Header(...)):
    if token != ACCESS_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido ou ausente")
