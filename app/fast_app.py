from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncpg
from config import DB_URL
from data_sources.storages.position_repository import PositionRepositorySQL, RepositoryStore, PositionRepositoryNoSQL, ManageRedis
from data_sources.storages.user_repository import UserRepositorySQL, UserRepositoryNoSQL




class Application():

    APPLICATION = None
    POOL = None

    @classmethod
    def create_application(cls) -> FastAPI:
        """Возвращает экземпляр приложения."""
        cls.APPLICATION = FastAPI(lifespan=lifespan)

    @classmethod
    def include_router(cls, router):
        cls.APPLICATION.include_router(router)

    @classmethod
    def get_application(cls):
        return cls.APPLICATION
    
    @classmethod
    async def get_pool(cls, app: FastAPI):
        return await app.state.async_session
    
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    #pool = await asyncpg.create_pool(host='localhost', user='kolya', password='1234', database='study_base20')
    #pool2 = await asyncpg.create_pool(host='localhost', user='kolya', password='1234', database='study_base20')
    RepositoryStore.user_repository = UserRepositoryNoSQL(ManageRedis())
    #RepositoryStore.user_repository = UserRepositorySQL(pool2)
    #app.state.async_session = await asyncpg.create_pool(host='localhost', user='kolya', password='1234', database='study_base20')
    yield
    await pool.close()