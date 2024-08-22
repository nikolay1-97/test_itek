"""Обработчик запроса на запрос определенного пользователя."""
from typing import Union

from fastapi import APIRouter
from fastapi import Request

from service.service_for_users import ServiceForUsers
from pydantic_models.user_models.get_user_resp import UserResp


get_user_router = APIRouter()

@get_user_router.get('/api/v1/users/{user_id}')
async def get_user(
    request: Request,
    user_id: str,
) -> Union[UserResp, bool]:
    """Запрос на получение данных пользователя.

    Parameters
    ----------
    requests: Request
        Объект Request.

    user_id: str
        id пользователя

    """
    
    return await ServiceForUsers.get(user_id)