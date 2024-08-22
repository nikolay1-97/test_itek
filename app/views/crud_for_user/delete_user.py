"""Обработчик запроса на удаление пользователя."""
from fastapi import APIRouter
from fastapi import Request

from service.service_for_users import ServiceForUsers


delete_user_router = APIRouter()

@delete_user_router.delete('/api/v1/users/{user_id}')
async def delete_user(
    request: Request,
    user_id: str,
) -> dict:
    """Запрос на удаление пользователя.

    Parameters
    ----------
    requests: Request
        Объект Request.

    user_id: str
        id пользователя

    """

    return await ServiceForUsers.delete(user_id)