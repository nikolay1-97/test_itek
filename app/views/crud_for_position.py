"""Модуль с функциями-обработчиками запросов."""
from fastapi import APIRouter, Depends
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from data_sources.models.user_model import get_async_session
from pydantic_models.position_models.position_model import PositionModel
from data_sources.storages.position_repository import RepositoryStore
from config import settings

position_router = APIRouter()

@position_router.post('/api/v1/positions')
async def create_position(
    request: PositionModel,
    session: AsyncSession = Depends(get_async_session),
):
    """Запрос на создание новой должности.

    Parameters
    ----------
    request: PositionModel
        Данные запроса.
        
    session: AsyncSession
        Сессия соединения с базой данных.
    """

    return await RepositoryStore.position_repository.create_position(request.title)


@position_router.patch('/api/v1/positions/{target_position_id}')
async def update_position(
    request: PositionModel,
    target_position_id: str,
    session: AsyncSession = Depends(get_async_session),
):
    """Запрос на обновление данных о должности.

    Parameters
    ----------
    requests: PositionModel
        Данные запроса.
        
    target_position_id: str
        id должности.

    session: AsyncSession
        Сессия соединения с базой данных.
    """

    return await RepositoryStore.position_repository.update_position(
        request.title,
        target_position_id,
    )


@position_router.get('/api/v1/positions/{position_id}')
async def get_position(
    request: Request,
    position_id: str,
):
    """Запрос на получение данных о должности.

    Parameters
    ----------
    requests: Request
        Объект Request.

    position_id: str
        id должности

    session: AsyncSession
        Сессия соединения с базой данных.
    """
    
    return await RepositoryStore.position_repository.get_position(position_id)


@position_router.delete('/api/v1/positions/{user_id}')
async def delete_position(
    request: Request,
    position_id: str,
):
    """Запрос на удаление должности.

    Parameters
    ----------
    requests: Request
        Объект Request.

    position_id: str
        id должности

    session: AsyncSession
        Сессия соединения с базой данных.
    """
    return await RepositoryStore.position_repository.delete_position(position_id)
