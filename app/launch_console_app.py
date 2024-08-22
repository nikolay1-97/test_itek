"""Модуль запуска консольного приложения."""
from asyncio import run

from service.service_for_positions import ServiceForPositions
from service.service_for_users import ServiceForUsers
from config.settings_store import SettingsStore
from console_app import ConsoleApp


async def launch_console_app() -> None:
    """Запускает консольное приложение."""

    if SettingsStore.get_settings('general_settings').get_settings('no_sql'):
        from data_sources.storages.position_repo.position_repo_no_sql import PositionRepositoryNoSQL
        from data_sources.storages.user_repo.user_repo_no_sql import UserRepositoryNoSQL
        from data_sources.storages.manage_redis.manage_redis import ManageRedis

        ServiceForPositions.set_repository(
            PositionRepositoryNoSQL(ManageRedis()),
        )
        ServiceForUsers.set_repository(
            UserRepositoryNoSQL(ManageRedis()),
        )
    else:
        from asyncpg import create_pool
        from data_sources.storages.position_repo.position_repo_sql import PositionRepositorySQL
        from data_sources.storages.user_repo.user_repo_sql import UserRepositorySQL
        pool = await create_pool(
            host = SettingsStore.get_settings('postgre_settings').get_settings('db_host'),
            user = SettingsStore.get_settings('postgre_settings').get_settings('db_user'),
            password = SettingsStore.get_settings('postgre_settings').get_settings('password'),
            database = SettingsStore.get_settings('postgre_settings').get_settings('db_name'),
        )
        ServiceForPositions.set_repository(
            PositionRepositorySQL(pool),
        )
        ServiceForUsers.set_repository(
            UserRepositorySQL(pool),
        )

    ConsoleApp.set_service('position', ServiceForPositions)
    ConsoleApp.set_service('user', ServiceForUsers)

    try:
        while True:
            await ConsoleApp.working_with_data()
    except KeyboardInterrupt:
        if not SettingsStore.get_settings('general_settings').get_settings(
            'is_console_app',
        ):
            await pool.close()

run(launch_console_app())