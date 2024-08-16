import asyncio
from asyncpg import create_pool
from data_sources.storages.position_repository import (
    PositionRepositorySQL,
    RepositoryStore,
    PositionRepositoryNoSQL,
    ManageRedis,
    SericeForUsers,
    SericeForPositions,
    ConsoleApp,
)
from data_sources.storages.user_repository import UserRepositoryNoSQL, UserRepositorySQL
from console_app import ConsoleApp


async def launch_console_app():
    pool = await create_pool(host='localhost', user='kolya', password='1234', database='study_base20')

    RepositoryStore.position_repository = PositionRepositoryNoSQL(ManageRedis())
    RepositoryStore.user_repository = UserRepositorySQL(pool)
    SericeForPositions.repository_store = RepositoryStore
    SericeForUsers.repository_store = RepositoryStore
    ConsoleApp.service_for_positions = SericeForPositions
    ConsoleApp.service_for_users = SericeForUsers

    while True:
        await ConsoleApp.input()

asyncio.run(launch_console_app())