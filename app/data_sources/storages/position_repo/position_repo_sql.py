"""Модуль содержит класс репозиторий 
для сущности должность с использованием
реляционной СУБД.
"""
from uuid import uuid4
from typing import Union

from asyncpg import Record

from data_sources.storages.position_repo.abstact_position_repo import PositionRepository
from pydantic_models.position_models.update_position_resp import (
    PositionUpdateResp,
)
from pydantic_models.position_models.get_position_model import PositionModelResp


class PositionRepositorySQL(PositionRepository):
    """Класс совершает CRUD операции с сущностью
    пользователь с
    использованием реляционной СУБД.
    
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
    ) -> Union[Record, bool]:
        """Возвращает должность по id.

        Parameters
        ----------
        position_id: str
            id должности.
            
        """
        
        try:
            async with self.session.acquire() as con:
                query = 'SELECT * FROM position WHERE id = ($1)'
                exists_position = await con.fetchrow(query, position_id)
                if exists_position is None:
                    return False
                return exists_position
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def get_position_by_title(
        self,
        title: str,
    ) -> Union[Record, bool]:
        """Возвращает должность по названию.

        Parameters
        ----------
        title: str
            Название должности.
            
        """

        try:
            async with self.session.acquire() as con:
                query = f'SELECT * FROM position WHERE title = ($1)'
                exists_position = await con.fetchrow(query, title)
                if exists_position is None:
                    return False
                return exists_position
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
            async with self.session.acquire() as con:
                await con.execute(
                    'INSERT INTO "position"(id, title) VALUES($1, $2)',
                    position_id,
                    title,
                )
                position = await self.get_position_by_title(title)
            
                return PositionModelResp(
                    id = position['id'],
                    title = position['title'],
                )
        except Exception as some_ex:
            print(some_ex)
            return {'message': 'error', 'detail': 'функция create_position'}
        
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
            async with self.session.acquire() as con:
                await con.execute(
                    'UPDATE position SET title = ($1) WHERE id = ($2)',
                    title,
                    position_id,
                )
                position = await self.get_position_by_id(position_id)
            
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
        
        position = await self.get_position_by_id(position_id)

        if not position:
                return False

        try:
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
            async with self.session.acquire() as con:
                await con.execute(
                    'DELETE FROM position WHERE id = ($1)',
                    position_id,
                )
            return {
                "status": True,
                "message": "Позиция успешно удалена"
            }
        except Exception as some_ex:
            print(some_ex)
            return 'error'