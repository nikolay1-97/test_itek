"""Обработчик запроса на запрос определенной должности."""
from typing import Union

from fastapi import APIRouter
from fastapi import Request

from service.service_for_positions import ServiceForPositions
from pydantic_models.position_models.get_position_model import PositionModelResp


get_position_router = APIRouter()

@get_position_router.get('/api/v1/positions/{position_id}')
async def get_position(
    request: Request,
    position_id: str,
) -> Union[PositionModelResp, bool]:
    """Запрос на получение данных о должности.

    Parameters
    ----------
    requests: Request
        Объект Request.

    position_id: str
        id должности

    """
    
    return await ServiceForPositions.get(position_id)