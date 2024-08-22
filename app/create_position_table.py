"""Модуль создания таблицы в базе данных для сущности должность"""
import psycopg2
from config.settings_store import SettingsStore


with psycopg2.connect(
    SettingsStore.get_settings('postgre_settings').get_db_url(),
) as conn:
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE position \
               (id VARCHAR(50) PRIMARY KEY,\
               title VARCHAR(50))',
    )