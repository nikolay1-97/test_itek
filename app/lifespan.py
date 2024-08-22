"""Модуль содержит функцию lifespan,
которая определяет логику при запуке и остановке fastapi приложения."""
from fastapi import FastAPI
from contextlib import asynccontextmanager

from service.service_for_positions import ServiceForPositions
from service.service_for_users import ServiceForUsers
from config.settings_store import SettingsStore

    
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Определяет логику при запуке и остановке fastapi приложения."""
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
        ServiceForUsers.set_repository(
            UserRepositorySQL(pool),
        )
        ServiceForPositions.set_repository(
            PositionRepositorySQL(pool),
        )
    yield
    if not SettingsStore.get_settings('general_settings').get_settings('no_sql'):
        await pool.close()