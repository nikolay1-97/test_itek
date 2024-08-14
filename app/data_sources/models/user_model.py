"""Модуль с моделями данных базы данных."""
import uuid

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    String,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.dialects.postgresql import UUID

from config import DB_URL


metadata = MetaData()

engine = create_async_engine(DB_URL)

async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_async_session():
    async with async_session_maker() as session:
        yield session

#Модель данных для сущности пользователь.
User_model = Table(
    "users",
    metadata,
    Column('id', String, primary_key=True, nullable=False, index=True),
    Column('surname', String, nullable=False),
    Column('name', String, nullable=False),
    Column('patronymic', String, nullable=False),
    Column('email', String, nullable=False, unique=True),
    Column('position', Integer, ForeignKey("position.id"), nullable=False)
)

Position_model = Table(
    'position',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('title', String, nullable=False, unique=True),
)
