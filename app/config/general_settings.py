"""Модуль содержит основную конфигурацию приложения."""
from pydantic_settings import BaseSettings, SettingsConfigDict

from config.paths_to_settings_files import PathToSettingsFiles


class GeneralSettings(BaseSettings):
    """Класс содержит основную конфигурацию приложения.
    Определяет тип используемой СУБД и
    тип запускаемого приложения(fastapi приложение или консольное)

    Attributes
    ----------
    is_console_app: bool
        будет ли запущено консольное приложение

    no_sql: bool
        будет ли выбрана нереляционная база данных

    model_cnfig: SettingsConfigDict
        экземпляр SettingsConfigDict
    
    Methods
    -------
    get_settings()
        Возвращает переменные окружения is_console_app и no_sql

    """
    
    is_console_app: bool
    no_sql: bool
    
    model_config = SettingsConfigDict(
        env_file=PathToSettingsFiles.get_path('general'),
        extra='ignore',
        env_file_encoding='utf-8')

    def get_settings(self, name: str) -> str:
        """Возвращает переменные окружения is_console_app и no_sql.

        Parameters
        ----------
        name: str
            имя запрашиваемых настроек
            
        """
        if name == 'is_console_app':
            return self.is_console_app
        
        elif name == 'no_sql':
            return self.no_sql