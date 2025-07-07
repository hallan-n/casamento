from database import Gift
from dto import AddGift, UpdateGift
from fastapi import APIRouter, Depends, HTTPException
from persistence import create, delete, read, update
from utils import verify_token

route = APIRouter(prefix="/gift", tags=["Presente"])


@route.post("/", response_model=Gift, dependencies=[Depends(verify_token)])
async def add_gift(gift: AddGift) -> Gift:
    """Insere um presente"""
    try:
        resp = await create(Gift(**gift.model_dump()))
        if not resp:
            raise HTTPException(403, "Erro ao inserir um presente")
        return resp
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Erro ao inserir um presente: {e}")


@route.get("/", response_model=Gift | list[Gift], tags=["Publico"])
async def get_gift(id: int = None) -> Gift | list[Gift]:
    """Consulta os presentes"""
    try:
        resp = await read(Gift, id)
        if not resp:
            raise HTTPException(404, "Presente não encontrado")
        return resp
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Erro ao consultar presente: {e}")


@route.delete("/", dependencies=[Depends(verify_token)])
async def delete_gift(id: int):
    """Deleta um presente"""
    try:
        gift = await read(Gift, id)
        if not gift:
            raise HTTPException(404, "Presente não encontrado")
        resp = await delete(gift)
        return {"success": resp}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Erro ao delete um presente: {e}")


@route.put("/", response_model=Gift, tags=["Publico"])
async def update_gift(gift: UpdateGift):
    """Deleta um presente"""
    try:
        has_gift = await read(Gift, gift.id)
        if not has_gift:
            raise HTTPException(404, "Presente não encontrado")
        resp = await update(Gift(**gift.model_dump()))
        return resp
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Erro ao delete um presente: {e}")
