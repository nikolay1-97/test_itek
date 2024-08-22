"""Обработчик запроса на обновление данных о пользователе."""
from typing import Union

from fastapi import APIRouter

from pydantic_models.user_models.user_model import UserModel
from service.service_for_users import ServiceForUsers
from pydantic_models.user_models.update_user_resp import UserUpdateResp


update_user_router = APIRouter()

@update_user_router.patch('/api/v1/users/{target_user_id}')
async def update_user(
    request: UserModel,
    target_user_id: str,
) -> Union[UserUpdateResp, dict]:
    """Запрос на обновление данных пользователя.

    Parameters
    ----------
    requests: UserModel
        Данные запроса.
        
    target_user_id: str
        id пользователя.

    """
    return await ServiceForUsers.update(
        surname = request.surname,
        name = request.name,
        patronymic = request.patronymic,
        email = request.email,
        position = request.position,
        user_id = target_user_id,
    )
