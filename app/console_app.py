


class ConsoleApp():
    service_for_positions = None
    service_for_users = None

    @classmethod
    async def input(cls):
        try:
            input1 = input('Введите имя сущности:')
            input2 = input('Выберите действие(create/update/get/delete)')
            input3 = input('Введите значения полей').split()
            if input1 == 'position':
                if input2 == 'create':
                    title = input3[0]
                    resp = await cls.service_for_positions.create(title = title)
                    print('Позиция успешно добавлена')
                    print(resp)

                elif input2 == 'update':
                    title = input3[0]
                    position_id = input3[1]
                    resp = await cls.service_for_positions.update(
                        title = title,
                        position_id = position_id,
                    )
                    print('Позиция успешно обновлена')
                    print(resp)

                elif input2 == 'get':
                    position_id = input3[0]
                    resp = await cls.service_for_positions.get(position_id = position_id)
                    print(resp)

                elif input2 == 'delete':
                    position_id = input3[0] 
                    resp = await cls.service_for_positions.delete(position_id = position_id)
                    print(resp)

            elif input1 == 'users':
                if input2 == 'create':
                    surname = input3[0]
                    name = input3[1]
                    patronymic = input3[2]
                    email = input3[3]
                    position = input3[4]

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
                    surname = input3[0]
                    name = input3[1]
                    patronymic = input3[2]
                    email = input3[3]
                    position = input3[4]
                    user_id = input3[5]
                
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
                    user_id = input3[0]
                    resp = await cls.service_for_users.get(user_id = user_id)
                    print(resp)

                elif input2 == 'delete':
                    user_id = input3[0]  
                    resp = await cls.service_for_users.delete(user_id = user_id)
                    print(resp)
        except Exception as some_ex:
            print(some_ex)
