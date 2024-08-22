"""Обработчик запроса на создание нового пользователя."""
from typing import Union

from fastapi import APIRouter

from pydantic_models.user_models.user_model import UserModel
from service.service_for_users import ServiceForUsers
from pydantic_models.user_models.get_user_resp import UserResp


create_user_router = APIRouter()

@create_user_router.post('/api/v1/users')
async def create_user(request: UserModel) -> Union[UserResp, dict]:
    """Запрос на создание нового пользователя.

    Parameters
    ----------
    request: UserModel
        Данные запроса.
        
    """

    return await ServiceForUsers.create(
        surname = request.surname,
        name = request.name,
        patronymic = request.patronymic,
        email = request.email,
        position = request.position,
    )