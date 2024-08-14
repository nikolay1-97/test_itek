"""Модуль содержит классы-репозитории с использованием SQL и
NoSQL СУБД.

"""
import uuid
import os
import subprocess

from fastapi import HTTPException, Depends
from starlette import status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic_models.position_models.update_position_resp import (
    PositionUpdateResp,
)
from pydantic_models.position_models.get_position_model import PositionModelResp
from data_sources.models.position_model import Position_model
from config import settings, redis_instance


class ManageRedis():
    def hset(self, *args):
        try:
            req = ["redis-cli", "hset", args[0]]
            req.extend(args[1:])
            subprocess.Popen(req, stdout=subprocess.PIPE).communicate()[0]
        except Exception as some_ex:
            print(some_ex)
            return 'error'

    def hget(self, key: str):
        try:
            req = ["redis-cli", "hgetall", key]
            resp = subprocess.Popen(req, stdout=subprocess.PIPE).communicate()[0]
            resp = resp.decode('utf-8')
            return resp.split('\n')
        except Exception as some_ex:
            print(some_ex)
            return 'error'
    
    def hdel(self, key: str):
        try:
            req = ["redis-cli", "DEL", key]
            subprocess.Popen(req, stdout=subprocess.PIPE).communicate()[0]
        except Exception as some_ex:
            print(some_ex)
            return 'error'







class RepositoryStore:
    position_repository = None
    user_repository = None



class PositionRepository():
    """Базовый класс для создания репозиториев.

    Methods
    -------
    __init__()
        Инициализотор класа.

    create_position()
        Добавляет новую должность в бд.

    get_position()
        Возвращает должность.

    update_user()
        Обновляет данные о должности.

    delete_user()
        Удаляет должность.
    """

    def __init__(self, session = None):
        """Инициализатор класса.

        Parameters
        ----------
        session: session
            Сессия соединения с базой данных.
        """

        self.session = session

    async def create_position(self):
        pass
    
    async def get_position(self):
        pass
    
    async def update_position(self):
        pass
    
    async def delete_position(self):
        pass


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
    ):
        """Возвращает должность по id.

        Parameters
        ----------
        position_id: str
            id должности.
            
        session: AsyncSession
            Сессия соединения с базой данных.
        """
        try:
            async with self.session.acquire() as con:
                query = f'SELECT * FROM position WHERE id = {position_id}'
                exists_position = await con.fetchrow(query)
                if exists_position is None:
                    return False
                return exists_position
        except Exception as some_ex:
            print(some_ex)
            return False
        
    async def get_position_by_title(
        self,
        title: str,
    ):
        """Возвращает должность по названию.

        Parameters
        ----------
        title: str
            Название должности.
            
        session: AsyncSession
            Сессия соединения с базой данных.
        """

        try:
            async with self.session.acquire() as con:
                query = f'SELECT * FROM position WHERE title = ($1)'
                exists_position = await con.fetchrow(query, title)
                print(f'Это новая позиция {exists_position}')
                if exists_position is None:
                    return False
                return exists_position
        except Exception as some_ex:
            print(some_ex)
            return False

    async def create_position(
        self,
        title: str,
    ):
        """Создает новую должность.

        Parameters
        ----------
        title: str
            Название должности.
            
        session: AsyncSession
            Сессия соединения с базой данных.
        """

        try:
            async with self.session.acquire() as con:
                await con.execute('INSERT INTO position (title) VALUES ($1)', title)
                position = await self.get_position_by_title(title)
            
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
    ):
        """Обновляет данные о должности.

        Parameters
        ----------
        title: str
            Название должности.

        position_id: str
            id должности.
            
        session: AsyncSession
            Сессия соединения с базой данных.
        """

        position = await self.get_position_by_id(position_id)

        if not position:
                return False

        try:
            async with self.session.acquire() as con:
                await con.execute(
                    'UPDATE position SET title = ($1) WHERE id = ($2)',
                    title,
                    int(position_id),
                )
                position = await self.get_position_by_id(position_id)
            
                return PositionUpdateResp(
                    id = position['id'],
                    new_title = position['title'],
                )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def get_position(self, position_id: str):
        """Возвращает должность по id.

        Parameters
        ----------
        position_id: str
            id должности.
            
        session: AsyncSession
            Сессия соединения с базой данных.
        """
        
        position = await self.get_position_by_id(position_id)

        if not position:
                return False

        try:
            return PositionModelResp(
                id=position['id'],
                title=position['title'],
            )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def delete_position(self, position_id: str):
        """Удаляет должность по id.

        Parameters
        ----------
        position_id: str
            id пользователя.

        session: AsyncSession
            Сессия соединения с базой данных.
        """

        if not self.delete:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Удаление данных запрещено",
            )
        exists_position = await self.get_position_by_id(position_id)

        if not exists_position:
            return False
        
        try:
            async with self.session.acquire() as con:
                await con.execute(
                    'DELETE FROM position WHERE id = ($1)', int(position_id)
                )
            return {
                "status": True,
                "message": "Позиция успешно удалена"
            }
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        







class PositionRepositoryNoSQL(PositionRepository):
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
    ):
        """Возвращает должность по id.

        Parameters
        ----------
        position_id: str
            id должности.
            
        session: AsyncSession
            Сессия соединения с базой данных.
        """
        try:
            position = self.session.hget(position_id)
            return {
                'id': position_id,
                'title': position[1],
            }
        except Exception as some_ex:
            print(some_ex)
            return False
        
    async def get_position_by_title(
        self,
        title: str,
    ):
        """Возвращает должность по названию.

        Parameters
        ----------
        title: str
            Название должности.
            
        session: AsyncSession
            Сессия соединения с базой данных.
        """

        try:
            return self.session.hget()
        except Exception as some_ex:
            print(some_ex)
            return False

    async def create_position(
        self,
        title: str,
    ):
        """Создает новую должность.

        Parameters
        ----------
        title: str
            Название должности.
            
        """

        try:
            position_id = str(uuid.uuid4())
            self.session.hset(position_id, 'title', title)
            return await self.get_position_by_id(position_id)
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def update_position(
        self,
        title: str,
        position_id: str,
    ):
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
            return {
                'id': position_id,
                'new_title': position['title']
            }
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def get_position(self, position_id: str):
        """Возвращает должность по id.

        Parameters
        ----------
        position_id: str
            id должности.
            
        """

        try:
            return await self.get_position_by_id(position_id)
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def delete_position(self, position_id: str):
        """Удаляет должность по id.

        Parameters
        ----------
        position_id: str
            id пользователя.

        """
        
        try:
            self.session.hdel(position_id)
            return 'Позиция успешно удалена'
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
#position_repository = PositionRepositorySQL(
        #settings.create,
        #settings.update,
        #settings.read,
        #settings.delete,
    #)