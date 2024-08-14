"""Файл запуска приложения."""
from fastapi import FastAPI
import uvicorn

from config import settings

from views.crud_for_users import user_router
from views.crud_for_position import position_router
from fast_app import Application


Application.create_application()
Application.include_router(user_router)
Application.include_router(position_router)

#def get_application() -> FastAPI:
    #"""Возвращает экземпляр приложения."""
    #application = FastAPI()
    #return application

#application = get_application()

#application.include_router(user_router)
#application.include_router(position_router)

if __name__ == '__main__':
    uvicorn.run(
        app=Application.get_application(),
        host=settings.app_host,
        port=int(settings.app_port),
    )