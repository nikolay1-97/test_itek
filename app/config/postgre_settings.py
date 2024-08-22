"""Модуль содержит конфигурацию для СУБД PostgreSQL."""
from pydantic_settings import BaseSettings, SettingsConfigDict

from config.paths_to_settings_files import PathToSettingsFiles


class PostgreSettings(BaseSettings):
    """Класс содержит конфигурацию работы приложения.

    Attributes
    ----------
    db_user: str
        имя пользователя базы данных

    password: str
        пароль базы данных

    db_host: str
        хост базы данных

    db_port: str
        порт базы данныз

    db_name: str
        имя базы данных

    model_cnfig: SettingsConfigDict
        экземпляр SettingsConfigDict
    
    Methods
    -------
    get_settings()
        Возвращает следующие настройки СУБД PostgreSQL:
            имя пользователя,
            пароль,
            хост,
            порт,
            имя базы.

    get_db_url()
        Возвращает URL базы данных.

    """
    
    db_user: str
    password: str
    db_host: str
    db_port: str
    db_name: str
    
    model_config = SettingsConfigDict(
        env_file=PathToSettingsFiles.get_path('postgre'),
        extra='ignore',
        env_file_encoding='utf-8',
    )

    def get_db_url(self) -> str:
        """Возвращает URL базы данных."""
        return f'postgresql://{self.db_user}:{self.password}@{self.db_host}:{self.db_port}/{self.db_name}'

    def get_settings(self, name: str) -> str:
        """Возвращает следующие настройки СУБД PostgreSQL:
            имя пользователя,
            пароль,
            хост,
            порт,
            имя базы данных.

        Parameters
        ----------
        name: str
            имя запрашиваемых настроек
            
        """
        if name == 'db_user':
            return self.db_user
        
        elif name == 'password':
            return self.password
        
        elif name == 'db_host':
            return self.db_host
        
        elif name == 'db_port':
            return self.db_port
        
        elif name == 'db_name':
            return self.db_name