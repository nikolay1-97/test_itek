"""Модуль с моделью данных для сущности должность."""
from sqlalchemy import (
    MetaData,
    Table,
    Column,
    String,
    Integer,
)


metadata = MetaData()

Position_model = Table(
    'position',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('title', String, nullable=False, unique=True),
)
