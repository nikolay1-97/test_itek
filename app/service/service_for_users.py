"""Модуль содержит класс сервис для сущности пользователь."""
from typing import Union

from service.abstract_service import Service
from pydantic_models.user_models.update_user_resp import UserUpdateResp
from pydantic_models.user_models.get_user_resp import UserResp

class ServiceForUsers(Service):
    """Класс сервис для сущности пользователь.

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
    async def create(cls, **kwargs: dict) -> Union[UserResp, dict]:
        """Создает нового пользователя.

        Parameters
        ----------
        kwargs: dict
            Словарь с данными.
            
        """
        try:
            is_user = await cls.get_repository().get_user_by_email(
                kwargs['email'],
            )

            if is_user:
                return {'message': 'Пользователь с таким email уже существует'}
            
            print('Пользователю отправлено приглашение на email')
            
            return await cls.get_repository().create_user(
                kwargs['surname'],
                kwargs['name'],
                kwargs['patronymic'],
                kwargs['email'],
                kwargs['position'],
            )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    @classmethod
    async def update(cls, **kwargs: dict) -> Union[UserUpdateResp, dict]:
        """Обновляет данные о пользователе.

        Parameters
        ----------
        kwargs: dict
            Словарь с данными.
            
        """
        try:
            is_user = await cls.get_repository().get_user_by_email(kwargs['email'])

            if is_user:
                return {'message': 'Пользователь с таким email уже существует'}
        
            return await cls.get_repository().update_user(
                    kwargs['surname'],
                    kwargs['name'],
                    kwargs['patronymic'],
                    kwargs['email'],
                    kwargs['position'],
                    kwargs['user_id'],
            )
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    @classmethod
    async def get(cls, user_id: str) -> Union[UserResp, bool]:
        """Возвращает пользователя по id.

        Parameters
        ----------
        user_id: str
            id пользователя.
            
        """
        try:
            return await cls.get_repository().get_user(user_id)
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    @classmethod
    async def delete(cls, user_id: str) -> dict:
        """Удаляет пользователя по id.

        Parameters
        ----------
        user_id: str
            id пользователя.
            
        """
        try:
            return await cls.get_repository().delete_user(user_id)
        except Exception as some_ex:
            print(some_ex)
            return 'error'