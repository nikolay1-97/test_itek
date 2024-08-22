"""Модуль содержит класс сервис для сущности должность."""
from typing import Union

from service.abstract_service import Service
from pydantic_models.position_models.update_position_resp import (
    PositionUpdateResp,
)
from pydantic_models.position_models.get_position_model import PositionModelResp

class ServiceForPositions(Service):
    """Класс сервис для сущности должность.

    Methods
    -------

    create()
        Создает запись в базу данных для конкретной сущности.

    update()
        Обновляет данные о сущности.

    get()
        Возвращает запрашиваемую запись из базы данных.

    delete()
        Удаляет запись из базы данных.

    """

    @classmethod
    async def create(cls, **kwargs: dict) -> PositionModelResp:
        """Создает новую запись в базе данных
        для сущности должность.

        Parameters
        ----------
        kwargs: dict
            Словарь с данными.
            
        """
        try:
            return await cls.get_repository().create_position(
                kwargs['title'],
            )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    @classmethod
    async def update(cls, **kwargs: dict) -> PositionUpdateResp:
        """Обновляет данные о должности.

        Parameters
        ----------
        kwargs: dict
            Словарь с данными.
            
        """
        try:
            return await cls.get_repository().update_position(
                kwargs['title'],
                kwargs['position_id']
            )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    @classmethod
    async def get(cls, position_id: str) -> Union[PositionModelResp, bool]:
        """Возвращает данные о должности по id.

        Parameters
        ----------
        position_id: str
            id должности.
            
        """
        try:
            return await cls.get_repository().get_position(
                position_id,
            )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    @classmethod
    async def delete(cls, position_id: str) -> dict:
        """ВУдаляет должность по id.

        Parameters
        ----------
        position_id: str
            id должности.
            
        """
        try:
            return await cls.get_repository().delete_position(
                position_id,
            )
        except Exception as some_ex:
            print(some_ex)
            return 'error'