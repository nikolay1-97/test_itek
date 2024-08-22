"""Обработчик запроса на обновление данных о должности."""
from fastapi import APIRouter

from pydantic_models.position_models.position_model import PositionModel
from service.service_for_positions import ServiceForPositions
from pydantic_models.position_models.update_position_resp import (
    PositionUpdateResp,
)


update_position_router = APIRouter()


@update_position_router.patch('/api/v1/positions/{target_position_id}')
async def update_position(
    request: PositionModel,
    target_position_id: str,
)-> PositionUpdateResp:
    """Запрос на обновление данных о должности.

    Parameters
    ----------
    requests: PositionModel
        Данные запроса.
        
    target_position_id: str
        id должности.

    """

    return await ServiceForPositions.update(
        title = request.title,
        position_id = target_position_id,
    )