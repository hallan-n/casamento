from uuid import UUID

from database import Guest
from dto import AddGuest, UpdateGuest
from fastapi import APIRouter, Depends, HTTPException
from persistence import create, delete, read, update
from pydantic import UUID4
from utils import verify_token

route = APIRouter(prefix="/guest", tags=["Convidado"])


@route.post("/", response_model=Guest, dependencies=[Depends(verify_token)])
async def add_guest(guest: AddGuest) -> Guest:
    """Insere um convidado"""
    try:
        resp = await create(Guest(**guest.model_dump()))
        if not resp:
            raise HTTPException(403, "Erro ao inserir um convidado")
        return resp
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Erro ao inserir um convidado: {e}")


@route.get("/", response_model=Guest | list[Guest], tags=["Publico"])
async def get_guest(id: UUID4 = None) -> Guest | list[Guest]:
    """Consulta os convidados"""
    try:
        resp = await read(Guest, id)
        if not resp:
            raise HTTPException(404, "Erro ao consultar um convidado")
        return resp
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Erro ao consultar convidado: {e}")


@route.delete("/", dependencies=[Depends(verify_token)])
async def delete_guest(id: UUID4):
    """Deleta um convidado"""
    try:
        guest = await read(Guest, id)
        if not guest:
            raise HTTPException(404, "convidado não encontrado")
        resp = await delete(guest)
        return {"success": resp}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Erro ao delete um convidado: {e}")


@route.put("/", response_model=Guest, tags=["Publico"])
async def update_guest(guest: UpdateGuest):
    """Deleta um convidado"""
    try:
        has_guest = await read(Guest, guest.id)
        if not has_guest:
            raise HTTPException(404, "Convidado não encontrado")
        resp = await update(Guest(**guest.model_dump()))
        return resp
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Erro ao delete um convidado: {e}")
