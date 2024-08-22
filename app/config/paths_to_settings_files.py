"""Модуль содержит класс в которым хранятся пути
до .env файлов с конфигурацией приложения.
"""
import os


class PathToSettingsFiles():
    """Класс содержит пути до .env файлов с конфигурацией
    работы приложения.

    Attributes
    ----------

    path_to_general_settings: str
        путь до .env файла с основынми настройками

    path_to_fastapi_app_settings: str
        путь до .env файла(хост и порт для fastapi приложения)

    path_to_postgre_settings: str
        путь до .env файла с настройками для PostgreSQL

    Methods
    -------
    get_path()
        Возвращает пути до .env файлов.

    """

    path_to_general_settings = os.path.dirname(
        os.path.realpath(__file__),
    )[:-10] + 'env_files/.env-gen-settings'

    path_to_fastapi_app_settings = os.path.dirname(
        os.path.realpath(__file__),
    )[:-10] + 'env_files/.env-fastapi-app-settings'

    path_to_postgre_settings = os.path.dirname(
        os.path.realpath(__file__),
    )[:-10] + 'env_files/.env-postgre-settings'

    @classmethod
    def get_path(cls, name: str) -> str:
        """Возвращает пути до .env файлов.

        Parameters
        ----------
        name: str
            имя запрашиваемых настроек
            
        """
        if name == 'general':
            return cls.path_to_general_settings
        
        elif name == 'fastapi':
            return cls.path_to_fastapi_app_settings
        
        elif name == 'postgre':
            return cls.path_to_postgre_settings
