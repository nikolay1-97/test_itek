"""Модель данных ответа для обновления данных о сущности должность."""
from pydantic import BaseModel


class PositionUpdateResp(BaseModel):
    """Модель данных для ответа для обновления
    сущности должнсть.
    """
    id: int
    new_title: str