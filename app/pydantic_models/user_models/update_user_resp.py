"""Модель данных ответа для обновления данных пользователя."""
from pydantic import BaseModel


class UserUpdateResp(BaseModel):
    """Модель данных ответа для обновления пользователя."""
    id: str
    new_surname: str
    new_name: str
    new_patronymic: str
    new_email: str
    new_position: str
