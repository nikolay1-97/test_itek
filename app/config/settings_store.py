"""Модуль содержит класс, который объединяет все настройки
работы приложения.
"""
from typing import Any

from config.general_settings import GeneralSettings
from config.paths_to_settings_files import PathToSettingsFiles


class SettingsStore():
    """Класс содержит основную конфигурацию приложения.
    Определяет тип используемой СУБД и
    тип запускаемого приложения(fastapi приложение или консольное).

    Attributes
    ----------
    general_settings: GeneralSettings
        основная конфигурация приложения

    fastapi_app_settings: FastApiAPPSettings
        конфигурация для работы fastapi приложения
        
    postgre_settings: PostgreSettings
        конфигурация работы СУБД PostgreSQL
    
    Methods
    -------
    get_settings()
        Возвращает конфигурацию работы приложения:
            основную конфигурацию,
            конфигурайию fastapi приложения,
            конфигурацию СУБД PostgreSQL. 

    """

    general_settings = GeneralSettings(
    _env_file=PathToSettingsFiles.get_path('general'),
    extra='ignore',
    env_file_encoding='utf-8',
)
    if not general_settings.get_settings('is_console_app'):
        from config.fastapi_app_settings import FastApiAPPSettings

        fastapi_app_settings = FastApiAPPSettings(
            _env_file=PathToSettingsFiles.get_path('fastapi'),
            extra='ignore',
            env_file_encoding='utf-8',
        )

    if not general_settings.get_settings('no_sql'):
        from config.postgre_settings import PostgreSettings

        postgre_settings = PostgreSettings(
            env_file=PathToSettingsFiles.get_path('postgre'),
            extra='ignore',
            env_file_encoding='utf-8',
        )

    @classmethod
    def get_settings(cls, name: str) -> Any:
        """Возвращает конфигурацию работы приложения:
            основную конфигурацию,
            конфигурайию fastapi приложения,
            конфигурацию СУБД PostgreSQL.

        Parameters
        ----------
        name: str
            имя запрашиваемых настроек
            
        """
        if name == 'general_settings':
            return cls.general_settings
        
        elif name == 'fastapi_app_settings':
            if cls.fastapi_app_settings:
                return cls.fastapi_app_settings
            
        elif name == 'postgre_settings':
            if cls.postgre_settings:
                return cls.postgre_settings
        