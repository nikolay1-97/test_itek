"""Модель данных для создания и обновления данных сущности должность."""
from pydantic import BaseModel


class PositionModel(BaseModel):
    """Модель данных для создания сущности должность."""
    title: str