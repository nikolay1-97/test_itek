"""Модуль запуска fastapi приложения."""
import uvicorn

from config.settings_store import SettingsStore
from views.crud_for_pos_s.create_positions import create_position_router
from views.crud_for_pos_s.update_position import update_position_router
from views.crud_for_pos_s.get_position import get_position_router
from views.crud_for_pos_s.delete_position import delete_position_router
from views.crud_for_user.create_user import create_user_router
from views.crud_for_user.get_user import get_user_router
from views.crud_for_user.update_user import update_user_router
from views.crud_for_user.delete_user import delete_user_router
from fast_app import Application



Application.create_application()
Application.include_router(create_position_router)
Application.include_router(update_position_router)
Application.include_router(get_position_router)
Application.include_router(delete_position_router)
Application.include_router(create_user_router)
Application.include_router(get_user_router)
Application.include_router(update_user_router)
Application.include_router(delete_user_router)


if __name__ == '__main__':
    uvicorn.run(
        app=Application.get_application(),
        host=SettingsStore.get_settings('fastapi_app_settings').get_settings('app_host'),
        port=int(SettingsStore.get_settings('fastapi_app_settings').get_settings('app_port')),
    )