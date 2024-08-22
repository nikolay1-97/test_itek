from fastapi import FastAPI, APIRouter
from lifespan import lifespan


class Application():
    """Класс содержит экземпляр fastapi приложения.

    Attributes
    ----------
    APPLICATION: FastAPI
        Экземпляр fastapi приложения.

    Methods
    -------
    create_application()
        Создает экземпляр fastapi приложения.

    include_router()
        Включает роутеры в fastapi приложение.

    get_application()
        Возвращает экземпляр fastapi приложения.

    """

    APPLICATION = None

    @classmethod
    def create_application(cls) -> None:
        """Создает экземпляр fastapi приложения."""
        cls.APPLICATION = FastAPI(lifespan=lifespan)

    @classmethod
    def include_router(cls, router: APIRouter) -> None:
        """Включает роутеры в fastapi приложение.

        Parameters
        ----------
        router: APIRouter
            Экземпляр класса APIRouter.
            
        """
        cls.APPLICATION.include_router(router)

    @classmethod
    def get_application(cls) -> FastAPI:
        """Возвращает экземпляр fastapi приложения."""
        return cls.APPLICATION
    