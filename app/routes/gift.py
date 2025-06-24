from fastapi import APIRouter, HTTPException

from dto import AddGift, UpdateGift
from database import Gift
from persistence import create, read, delete, update

route = APIRouter(prefix='/gift', tags=['Presente'])

@route.post('/')
async def add_gift(gift: AddGift):
    """Insere um presente"""
    try:
        resp = await create(Gift(**gift.model_dump()))
        if not resp:
            raise HTTPException(403, 'Erro ao inserir um presente')
        return resp
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f'Erro ao inserir um presente: {e}')

@route.get('/')
async def get_gift(id: int = None):
    """Consulta os presentes"""
    try:
        resp = await read(Gift, id)
        if not resp:
            raise HTTPException(404, 'Erro ao consultar um presente')
        return resp
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f'Erro ao consultar presente: {e}')

@route.delete('/')
async def delete_gift(id: int):
    """Deleta um presente"""
    try:
        gift = await read(Gift, id)
        if not gift:
            return HTTPException(404, 'Presente não encontrado')
        resp = await delete(gift)
        return {'success': resp}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f'Erro ao delete um presente: {e}')


@route.put('/')
async def update_gift(gift: UpdateGift):
    """Deleta um presente"""
    try:
        has_gift = await read(Gift, gift.id)
        if not has_gift:
            return HTTPException(404, 'Presente não encontrado')
        resp = await update(Gift(**gift.model_dump()))
        return resp
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f'Erro ao delete um presente: {e}')

