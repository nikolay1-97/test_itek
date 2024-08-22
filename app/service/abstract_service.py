"""Модуль содержит базовый класс сервис."""
from typing import Any

class Service():
    """Базовый класс сервис.

    Attributes
    ----------
    repository: None
        Репозитрий для сервиса

    Methods
    -------
    set_repository()
        Устанавливает репозиторий для сервиса.

    get_repository()
        Возвращает репозиторий сервиса.

    create()
        Создает запись в базу данных для конкретной сущности.

    update()
        Обновляет данные о сущности.

    get()
        Возвращает запрашиваемую запись из базы данных.

    delete()
        Удаляет запись из базы данных.

    """

    repository = None

    @classmethod
    def set_repository(cls, repository: Any) -> None:
        cls.repository = repository

    @classmethod
    def get_repository(cls) -> Any:
        return cls.repository

    @classmethod
    async def create(cls, *args) -> Any:
        pass

    @classmethod
    async def update(cls, *args) -> Any:
        pass

    @classmethod
    async def get(cls, key: str) -> Any:
        pass

    @classmethod
    async def delete(cls, key: str) -> Any:
        pass