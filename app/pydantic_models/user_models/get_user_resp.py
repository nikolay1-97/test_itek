"""Модель данных ответа для запроса пользователя."""
from pydantic import BaseModel


class UserResp(BaseModel):
    """Модель данных ответа для запроса пользователя."""
    id: str
    surname: str
    name: str
    patronymic: str
    email: str
    position: str