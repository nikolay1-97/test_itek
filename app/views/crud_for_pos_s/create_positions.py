"""Обрабочик запроса на добавление должности."""
from fastapi import APIRouter

from pydantic_models.position_models.position_model import PositionModel
from pydantic_models.position_models.get_position_model import PositionModelResp
from service.service_for_positions import ServiceForPositions


create_position_router = APIRouter()

@create_position_router.post('/api/v1/positions')
async def create_position(
    request: PositionModel,
) -> PositionModelResp:
    """Запрос на создание новой должности.

    Parameters
    ----------
    request: PositionModel
        Данные запроса.
        
    """

    return await ServiceForPositions.create(title = request.title)