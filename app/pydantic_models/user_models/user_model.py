"""Модель данных для создания и обновления данных пользователя."""
from pydantic import BaseModel


class UserModel(BaseModel):
    """Модель данных для создания пользователя."""
    surname: str
    name: str
    patronymic: str
    email: str
    position: str