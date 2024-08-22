"""Модуль содержит конфигурацию для запуска fastapi приложения."""
from pydantic_settings import BaseSettings, SettingsConfigDict

from config.paths_to_settings_files import PathToSettingsFiles


class FastApiAPPSettings(BaseSettings):
    """Класс содержит конфигурацию работы приложения.

    Attributes
    ----------

    app_host: str
        хост для запуска приложения

    app_port: str
        порт для запуска приложения

    model_cnfig: SettingsConfigDict
        экземпляр SettingsConfigDict

    Methods
    -------
    get_settings()
        Возвращает хост и порт.

    """
    
    app_host: str
    app_port: str
    
    model_config = SettingsConfigDict(
        env_file = PathToSettingsFiles.get_path('fastapi'),
        extra = 'ignore',
        env_file_encoding='utf-8',
    )

    def get_settings(self, name: str) -> str:
        """Возвращает хост и порт.

        Parameters
        ----------
        name: str
            имя запрашиваемых настроек
            
        """
        if name == 'app_host':
            return self.app_host
        
        elif name == 'app_port':
            return self.app_port
        