"""Модуль содержит класс репозиторий с использование нереляционной
СУБД для сущности должность.
"""
from uuid import uuid4
from typing import Union

from data_sources.storages.position_repo.abstact_position_repo import PositionRepository
from pydantic_models.position_models.update_position_resp import (
    PositionUpdateResp,
)
from pydantic_models.position_models.get_position_model import PositionModelResp


class PositionRepositoryNoSQL(PositionRepository):
    """Класс совершает CRUD операции с сущностью
    пользователь с
    использованием нереляционной СУБД.
    
    Methods
    -------
    get_position_by_id()
        Возвращает должность по id.
    
    create_position()
        Создает новую должность.
    
    update_position()
        Обновляет данные должности.

    get_position()
        Возвращает должность по id.

    delete_position()
        Удаляет должность.

    """

    async def get_position_by_id(
        self, position_id: str,
    ) -> Union[dict, bool]:
        """Возвращает должность по id.

        Parameters
        ----------
        position_id: str
            id должности.

        """
        try:
            position = self.session.hget(position_id)
            if not position:
                return False
            return {
                'id': position_id,
                'title': position[1],
            }
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def get_position_by_title(
        self,
        title: str,
    ) -> Union[list, bool]:
        """Возвращает должность по названию.

        Parameters
        ----------
        title: str
            Название должности.
            
        """

        try:
            return self.session.hget()
        except Exception as some_ex:
            print(some_ex)
            return False

    async def create_position(
        self,
        title: str,
    ) -> PositionModelResp:
        """Создает новую должность.

        Parameters
        ----------
        title: str
            Название должности.
            
        """

        try:
            position_id = str(uuid4())
            self.session.hset(position_id, 'title', title)
            position = await self.get_position_by_id(position_id)

            return PositionModelResp(
                    id = position['id'],
                    title = position['title'],
                )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def update_position(
        self,
        title: str,
        position_id: str,
    ) -> PositionUpdateResp:
        """Обновляет данные о должности.

        Parameters
        ----------
        title: str
            Название должности.

        position_id: str
            id должности.
            
        """

        try:
            self.session.hset(position_id, 'title', title)
            position =  await self.get_position_by_id(position_id)

            return PositionUpdateResp(
                    id = position['id'],
                    new_title = position['title'],
                )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def get_position(
        self,
        position_id: str,
    ) -> Union[PositionModelResp, bool]:
        """Возвращает должность по id.

        Parameters
        ----------
        position_id: str
            id должности.
            
        """

        try:
            position = await self.get_position_by_id(position_id)

            if not position:
                return False
            
            return PositionModelResp(
                id = position['id'],
                title = position['title'],
            )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def delete_position(self, position_id: str) -> dict:
        """Удаляет должность по id.

        Parameters
        ----------
        position_id: str
            id пользователя.

        """
        
        try:
            self.session.hdel(position_id)
            return {'message': 'Позиция успешно удалена'}
        except Exception as some_ex:
            print(some_ex)
            return 'error'