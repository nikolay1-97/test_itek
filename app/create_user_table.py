"""Модуль создания таблицы в базе данных для сущности пользователь."""
import psycopg2
from config.settings_store import SettingsStore


with psycopg2.connect(
    SettingsStore.get_settings('postgre_settings').get_db_url(),
) as conn:
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE users \
                 (id VARCHAR(50) PRIMARY KEY,\
                 surname VARCHAR(100),\
                 name VARCHAR(100),\
                 patronymic VARCHAR(100),\
                 email VARCHAR(100),\
                 position VARCHAR(100))',
    )
