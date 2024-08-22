"""Модуль содержит класс репозиторий
для сущности пользователь
с использование нереляционной СУБД.
"""
from uuid import uuid4
from typing import Union

from pydantic_models.user_models.update_user_resp import UserUpdateResp
from pydantic_models.user_models.get_user_resp import UserResp
from data_sources.storages.user_repo.abstract_user_repo import UserRepository


class UserRepositoryNoSQL(UserRepository):
    """Класс совершает CRUD операции с сущностью
    пользователь с
    использованием нереляционной СУБД.

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

    async def get_user_by_id(self, user_id: str) -> Union[dict, bool]:
        """Возвращает пользователя по id.

        Parameters
        ----------
        user_id: str
            id пользователя.
            
        """

        try:
            user = self.session.hget(user_id)
            if not user:
                return False
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
            return 'error'
        
    async def get_user_by_email(self, email: str) -> bool:
        """Возвращает пользователя по id.

        Parameters
        ----------
        user_id: str
            id пользователя.
            
        """

        try:
            user = self.session.get(email)
            if not user:
                return False
            return True
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    async def get_user(self, user_id: str) -> Union[UserResp, bool]:
        """Возвращает пользователя по id.

        Parameters
        ----------
        user_id: str
            id пользователя.
            
        """

        try:
            user = await self.get_user_by_id(user_id)
            if not user:
                return False
            
            return UserResp(
                id = user['id'],
                surname = user['surname'],
                name = user['name'],
                patronymic = user['patronymic'],
                email = user['email'],
                position = user['position']
            )
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
    ) -> UserResp:
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
            user_id = str(uuid4())
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

            self.session.set(email, email)

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
    ) -> UserUpdateResp:
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
            self.session.set(email, email)

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
            

    async def delete_user(self, user_id: str) -> dict:
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