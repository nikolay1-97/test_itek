"""Модуль содержит базовый класс репозитория для сущности должность."""
from typing import Any


class PositionRepository():
    """Базовый класс репозитория для сущности должность.

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

    def __init__(self, session: Any):
        """Инициализатор класса.

        Parameters
        ----------
        session: session
            Сессия соединения с базой данных.
        """

        self.session = session

    async def create_position(self) -> Any:
        pass
    
    async def get_position(self) -> Any:
        pass
    
    async def update_position(self) -> Any:
        pass
    
    async def delete_position(self) -> Any:
        pass
