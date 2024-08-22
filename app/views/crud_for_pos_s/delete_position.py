"""Обработчик запроса на удаление должности."""
from fastapi import APIRouter
from fastapi import Request

from service.service_for_positions import ServiceForPositions


delete_position_router = APIRouter()

@delete_position_router.delete('/api/v1/positions/{user_id}')
async def delete_position(
    request: Request,
    position_id: str,
) -> dict:
    """Запрос на удаление должности.

    Parameters
    ----------
    requests: Request
        Объект Request.

    position_id: str
        id должности

    """
    return await ServiceForPositions.delete(position_id)