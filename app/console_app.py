"""Модуль содержит класс,
реализующий работу консольного приложения.
"""
from typing import Any


class ConsoleApp():
    """Класс содержит логику работы консольного приложения.

    Attributes
    ----------
    service_for_positions: None
        сервис для сущности должность

    service_for_users: None
        сервис для сущности пользователь
    
    Methods
    -------
    set_service()
        Устанавливает сервисы для соответствующих сущностей.

    """
    service_for_positions = None
    service_for_users = None

    @classmethod
    def set_service(
        cls, name: str,
        service: Any,
    ) -> None:
        """Устанавливает сервис для определенной сущности.

        Parameters
        ----------
        name: str
            Имя сервиса.

        service: ServiceForPositions | ServiceForUsers
            Сервисы для соответствующих сущностей.
            
        """
        if name == 'position':
            cls.service_for_positions = service

        elif name == 'user':
            cls.service_for_users = service

    @classmethod
    async def working_with_data(cls) -> None:
        """Запрашивает данные через пользовательский ввод
        и передает полученные данные сервисам
        для создания, обновления, чтения, удаления данных
        соответствующих сущностей.
            
        """
        try:
            input1 = input('Введите имя сущности(position, user): ')
            input2 = input('Выберите действие(create/update/get/delete): ')
            if input1 == 'position':
                if input2 == 'create':
                    title = input('Введите значениe(название должности): ')
                    resp = await cls.service_for_positions.create(title = title)
                    print('Позиция успешно добавлена')
                    print(resp)

                elif input2 == 'update':
                    input3 = input(
                        'Введите значения через пробел(название должности id должности): ',
                    ).split()
                    title = input3[0]
                    position_id = input3[1]
                    resp = await cls.service_for_positions.update(
                        title = title,
                        position_id = position_id,
                    )
                    print('Позиция успешно обновлена')
                    print(resp)

                elif input2 == 'get':
                    position_id = input('Введите значение(id должности): ')
                    resp = await cls.service_for_positions.get(position_id = position_id)
                    print(resp)

                elif input2 == 'delete':
                    position_id = position_id = input('Введите значение(id должности): ') 
                    resp = await cls.service_for_positions.delete(position_id = position_id)
                    print(resp)

            elif input1 == 'user':
                if input2 == 'create':
                    surname = input('введите фамилию: ')
                    name = input('введите имя: ')
                    patronymic = input('введите отчество: ')
                    email = input('введите email: ')
                    position = input('введите id должности: ')

                    resp = await cls.service_for_users.create(
                        surname = surname,
                        name = name,
                        patronymic = patronymic,
                        email = email,
                        position = position,
                    )
                    print('Позиция успешно добавлена')
                    print(resp)

                elif input2 == 'update':
                    surname = input('введите фамилию: ')
                    name = input('введите имя: ')
                    patronymic = input('введите отчество: ')
                    email = input('введите email: ')
                    position = input('введите id должности: ')
                    user_id = input('введите id пользователя: ')
                
                    resp = await cls.service_for_users.update(
                        surname = surname,
                        name = name,
                        patronymic = patronymic,
                        email = email,
                        position = position,
                        user_id = user_id,
                    )
                    print('Позиция успешно обновлена')
                    print(resp)

                elif input2 == 'get':
                    user_id = input('введите id пользователя: ')
                    resp = await cls.service_for_users.get(user_id = user_id)
                    print(resp)

                elif input2 == 'delete':
                    user_id = input('введите id пользователя: ')
                    resp = await cls.service_for_users.delete(user_id = user_id)
                    print(resp)
        except Exception as some_ex:
            print(some_ex)
