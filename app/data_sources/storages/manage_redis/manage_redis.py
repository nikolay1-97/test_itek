from subprocess import Popen, PIPE
from typing import Union


class ManageRedis():
    """Класс для работы с Redis.

    Methods
    -------
    hset()
        Записывает множество

    hget()
        Возвращает множество

    hdel()
        Удаляет множество

    set()
        Записывет значение по ключу

    get()
        Возврящает значение по ключу

    """

    def hset(self, *args: tuple) -> None:
        """Записывает новое множество.

        Parameters
        ----------
        args: tuple
            Кортеж с данными.
            
        """
        try:
            req = ["redis-cli", "hset", args[0]]
            req.extend(args[1:])
            Popen(req, stdout = PIPE).communicate()[0]
        except Exception as some_ex:
            print(some_ex)
            return 'error'

    def hget(self, key: str) -> Union[list, bool]:
        """Возвращает множество.

        Parameters
        ----------
        key: str
            Запрашиваемый ключ.
            
        """
        try:
            req = ["redis-cli", "hgetall", key]
            resp = Popen(req, stdout = PIPE).communicate()[0]
            resp = resp.decode('utf-8').split('\n')
            if resp[0] == '':
                return False
            return resp
        except Exception as some_ex:
            print(some_ex)
            return 'error'
    
    def hdel(self, key: str) -> None:
        """Удаляет множество.

        Parameters
        ----------
        key: str
            Запрашиваемый ключ.
            
        """
        try:
            req = ["redis-cli", "DEL", key]
            Popen(req, stdout = PIPE).communicate()[0]
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    def set(self, key: str, value: str) -> None:
        """Записывет значение по ключу.

        Parameters
        ----------
        key: str
            Ключ.

        value: str
            Значение.
            
        """
        try:
            req = ["redis-cli", "set", key, value]
            Popen(req, stdout = PIPE).communicate()[0]
        except Exception as some_ex:
            print(some_ex)
            return 'error'
        
    def get(self, key: str) -> Union[list, bool]:
        """Возвращает значение по ключу.

        Parameters
        ----------
        key: str
            Запрашиваемый ключ.
    
        """
        try:
            req = ["redis-cli", "get", key]
            resp = Popen(req, stdout = PIPE).communicate()[0]
            resp = resp.decode('utf-8').split('\n')
            if resp[0] == '':
                return False
            return resp
        except Exception as some_ex:
            print(some_ex)
            return 'error'