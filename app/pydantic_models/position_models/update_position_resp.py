"""Модель данных ответа для обновления данных сущности должность."""
from pydantic import BaseModel


class PositionUpdateResp(BaseModel):
    """Модель данных для ответа для обновления
    сущности должнсть.
    """
    id: str
    new_title: str