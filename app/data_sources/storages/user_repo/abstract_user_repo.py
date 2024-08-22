"""Модуль содержит базовый класс репозиторий
для сущности пользователь.
"""
from typing import Any

class UserRepository():
    """Базовый класс дрепозитория для сущности пользователь.

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

    def __init__(self, session: Any):
        """Инициализатор класса.

        Parameters
        ----------
        session: session
            Сессия соединения с базой данных.
        """

        self.session = session

    async def create_user(self) -> Any:
        pass
    
    async def get_user(self) -> Any:
        pass
    
    async def update_user(self) -> Any:
        pass
    
    async def delete_user(self) -> Any:
        pass