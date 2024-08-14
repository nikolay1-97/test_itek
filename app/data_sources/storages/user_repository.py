"""Модуль содержит классы-репозитории с использованием SQL и
NoSQL СУБД.

"""
import uuid

from fastapi import HTTPException
from starlette import status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic_models.user_models.user_model import UserModel
from pydantic_models.user_models.update_user_resp import UserUpdateResp
from pydantic_models.user_models.get_user_resp import UserResp
from data_sources.models.user_model import User_model
from config import settings, redis_instance



class UserRepository():
    """Базовый класс для создания репозиториев.

    Methods
    -------
    __init__()
        Инициализотор класа.

    create_user()
        Добавляет нового пользователя в бд.

    get_user()
        Возвращает пользователя.

    update_user()
        Обновляет данные пользователя.

    delete_user()
        Удаляет пользователя.
    """

    def __init__(self, session):
        """Инициализатор класса.

        Parameters
        ----------
        session: session
            Сессия соединения с базой данных.
        """

        self.session = session

    async def create_user(self):
        pass
    
    async def get_user(self):
        pass
    
    async def update_user(self):
        pass
    
    async def delete_user(self):
        pass


class UserRepositorySQL(UserRepository):
    """Класс совершает CRUD операции с сущностью
    пользователь с
    использованием реляционной СУБД.
    
    Methods
    -------
    get_user_by_id()
        Возвращает пользователя по id.
    
    create_user()
        Создает нового пользователя.
    
    update_user()
        Обновляет данные пользователя.

    get_user()
        Возвращает пользователя по id.

    delete_user()
        Удаляет пользователя.

    """

    async def get_user_by_id(self, user_id: str):
        """Возвращает пользователя по id.

        Parameters
        ----------
        user_id: str
            id пользователя.
        """
        user_id = str(user_id)
        try:
            async with self.session.acquire() as con:
                query = 'SELECT * FROM users WHERE id = ($1)'
                exists_user = await con.fetchrow(query, user_id)
                if exists_user is None:
                    return False
                return exists_user
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def get_user_by_email(self, email: str):
        """Возвращает пользователя по email.

        Parameters
        ----------
        email: str
            email пользователя.
        """

        try:
            async with self.session.acquire() as con:
                query = 'SELECT * FROM users WHERE email = ($1)'
                exists_user = await con.fetchrow(query, email)
                if exists_user is None:
                    return False
                return exists_user
        except Exception as some_ex:
            print(some_ex)
            return 'error'

    async def create_user(
        self,
        surname: str,
        name: str,
        patronymic: str,
        email: str,
        position: str,
    ):
        """Создает нового пользователя.

        Parameters
        ----------
        surname: str
            Фамилия пользователя.

        name: str
            Имя пользователя.
        
        patronymic: str
            Отчество пользователя.
        
        """
        
        try:
            user_id = str(uuid.uuid4())
            async with self.session.acquire() as con:
                await con.execute(
                    'INSERT INTO "users"(id, surname, name, patronymic, email, position)\
                    VALUES($1, $2, $3, $4, $5, $6)',
                    user_id,
                    surname,
                    name,
                    patronymic,
                    email,
                    int(position),
                )
                user = await self.get_user_by_id(user_id)

                return UserResp(
                    id = user['id'],
                    surname = user['surname'],
                    name = user['name'],
                    patronymic = user['patronymic'],
                    email = user['email'],
                    position = user['position'],
                )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def update_user(
        self,
        surname: str,
        name: str,
        patronymic: str,
        email: str,
        position: str,
        user_id: str,
    ):
        """Обновляет данные пользователя.

        Parameters
        ----------
        surname: str
            Фамилия пользователя.

        name: str
            Имя пользователя.
        
        patronymic: str
            Отчество пользователя.

        user_id: str
            id пользователя.
            
        """

        try:
            async with self.session.acquire() as con:
                await con.execute(
                    'UPDATE users SET surname = ($1), name = ($2), patronymic = ($3),\
                    email = ($4), position = ($5) WHERE id = ($6)',
                    surname,
                    name,
                    patronymic,
                    email,
                    int(position),
                    user_id,
                )
            user = await self.get_user_by_id(user_id)

            return UserUpdateResp(
                id=user['id'],
                new_surname=user['surname'],
                new_name=user['name'],
                new_patronymic=user['patronymic'],
                new_email = user['email'],
                new_position = user['position'],
            )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def get_user(self, user_id: str):
        """Возвращает пользователя по id.

        Parameters
        ----------
        user_id: str
            id пользователя.
            
        """
        user = await self.get_user_by_id(user_id)
        
        try:
            return UserResp(
                id=user['id'],
                surname=user['surname'],
                name=user['name'],
                patronymic=user['patronymic'],
                email=user['email'],
                position=user['position'],
            )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def delete_user(self, user_id: str):
        """Удаляет пользователя по id.

        Parameters
        ----------
        user_id: str
            id пользователя.

        """

        try:
            async with self.session.acquire() as con:
                await con.execute('DELETE FROM users WHERE id = ($1)', user_id)
                return {'message': 'пользователь успешно удален'}
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        

class UserRepositoryNoSQL(UserRepository):
    """Класс совершает CRUD операции с сущностью
    пользователь с
    использованием NoSQL СУБД.

    Attributes
    ----------
    
    Methods
    -------
    get_user_by_id()
        Возвращает пользователя по id.
    
    create_user()
        Создает нового пользователя.
    
    update_user()
        Обновляет данные пользователя.

    get_user()
        Возвращает пользователя по id.

    delete_user()
        Удаляет пользователя.

    """

    async def get_user_by_id(self, user_id: str):
        """Возвращает пользователя по id.

        Parameters
        ----------
        user_id: str
            id пользователя.
            
        """

        try:
            user = self.session.hget(user_id)
            return {
                'id': user_id,
                'surname': user[1],
                'name': user[3],
                'patronymic': user[5],
                'email': user[7],
                'position': user[9],
            }
        except Exception as some_ex:
            print(some_ex)
            return False
        
    async def get_user(self, user_id: str):
        """Возвращает пользователя по id.

        Parameters
        ----------
        user_id: str
            id пользователя.
            
        """

        try:
            return await self.get_user_by_id(user_id)
        except Exception as some_ex:
            print(some_ex)
            return 'error'

    async def create_user(
        self,
        surname: str,
        name: str,
        patronymic: str,
        email: str,
        position: str,
    ):
        """Создает нового пользователя.

        Parameters
        ----------
        surname: str
            Фамилия пользователя.

        name: str
            Имя пользователя.
        
        patronymic: str
            Отчество пользователя.
        """

        try:
            user_id = str(uuid.uuid4())
            self.session.hset(
                user_id,
                'surname',
                surname,
                'name',
                name,
                'patronymic',
                patronymic,
                'email',
                email,
                'position',
                str(position),
            )
            user = await self.get_user_by_id(user_id)
            return UserResp(
                id = user['id'],
                surname = user['surname'],
                name = user['name'],
                patronymic = user['patronymic'],
                email = user['email'],
                position = user['position'],
            )
        except Exception as some_ex:
            print(some_ex)
            return 'error'

    async def update_user(
        self,
        surname: str,
        name: str,
        patronymic: str,
        email: str,
        position: str,
        user_id: str,
    ):
        """Обновляет данные пользователя.

        Parameters
        ----------
        surname: str
            Фамилия пользователя.

        name: str
            Имя пользователя.
        
        patronymic: str
            Отчество пользователя.

        user_id: str
            id пользователя.
        """

        try:
            self.session.hset(
                user_id,
                'surname',
                surname,
                'name',
                name,
                'patronymic',
                patronymic,
                'email',
                email,
                'position',
                str(position),
            )
            user = await self.get_user_by_id(user_id)
            return UserUpdateResp(
                id = user['id'],
                new_surname = user['surname'],
                new_name = user['name'],
                new_patronymic = user['patronymic'],
                new_email = user['email'],
                new_position = user['position'],
            )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
            

    async def delete_user(self, user_id: str):
        """Удаляет пользователя по id.

        Parameters
        ----------
        user_id: str
            id пользователя.
        """
        
        try:
            self.session.hdel(user_id)
            return {'message': 'Пользователь успешно удален'}
        except Exception as some_ex:
            print(some_ex)
            return 'error'
 