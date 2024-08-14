"""Модуль с функциями-обработчиками запросов."""
from fastapi import APIRouter, Depends
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from data_sources.models.user_model import get_async_session
from pydantic_models.user_models.user_model import UserModel
from data_sources.storages.position_repository import RepositoryStore
from config import settings


user_router = APIRouter()

@user_router.post('/api/v1/users')
async def create_user(request: UserModel):
    """Запрос на создание нового пользователя.

    Parameters
    ----------
    request: UserModel
        Данные запроса.
        
    """
    return await RepositoryStore.user_repository.create_user(
        request.surname,
        request.name,
        request.patronymic,
        request.email,
        request.position,
    )


@user_router.patch('/api/v1/users/{target_user_id}')
async def update_user(
    request: UserModel,
    target_user_id: str,
):
    """Запрос на обновление данных пользователя.

    Parameters
    ----------
    requests: UserModel
        Данные запроса.
        
    target_user_id: str
        id пользователя.

    """
    return await RepositoryStore.user_repository.update_user(
        request.surname,
        request.name,
        request.patronymic,
        request.email,
        request.position,
        target_user_id,
    )


@user_router.get('/api/v1/users/{user_id}')
async def get_user(
    request: Request,
    user_id: str,
):
    """Запрос на получение данных пользователя.

    Parameters
    ----------
    requests: Request
        Объект Request.

    user_id: str
        id пользователя

    """
    
    return await RepositoryStore.user_repository.get_user(user_id)


@user_router.delete('/api/v1/users/{user_id}')
async def delete_user(
    request: Request,
    user_id: str,
):
    """Запрос на удаление пользователя.

    Parameters
    ----------
    requests: Request
        Объект Request.

    user_id: str
        id пользователя

    """

    return await RepositoryStore.user_repository.delete_user(user_id)
