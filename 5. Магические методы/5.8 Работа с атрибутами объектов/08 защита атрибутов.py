"""
Будем считать атрибут защищенным, если его имя начинается с символа нижнего подчеркивания (_).
    Например, _password, __email и __dict__.

Реализуйте класс ProtectedObject. При создании экземпляра класс должен принимать произвольное количество именованных
    аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Класс ProtectedObject должен запрещать получать и изменять значения защищенных атрибутов своих экземпляров,
    а также удалять эти атрибуты. При попытке получить или изменить значение защищенного атрибута,
    а также попытке удалить атрибут, должно возбуждаться исключение AttributeError с текстом:

    Доступ к защищенному атрибуту невозможен

Примечание 1. Дополнительная проверка данных на корректность не требуется.
    Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса ProtectedObject нет, она может быть произвольной.
"""


class ProtectedObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        if item[0] == "_":
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key[0] == "_":
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item[0] == "_":
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        else:
            object.__delattr__(self, item)


# INPUT DATA:

# TEST_1:
print("\nтест 1")
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)

# TEST_2:
print("\nтест 2")
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    user._password = 'qwerty12345'
except AttributeError as e:
    print(e)

# TEST_3:
print("\nтест 3")
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    del user._password
except AttributeError as e:
    print(e)

# TEST_4:
print("\nтест 4")
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

del user.login
print('Успешное удаление атрибута')

# TEST_5:
print("\nтест 5")
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')
print(object.__getattribute__(user, 'login'))
print(object.__getattribute__(user, '_password'))

# TEST_6:
print("\nтест 6")
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    user.__dict__['attr'] = 1
except AttributeError as e:
    print(e)

# TEST_7:
print("\nтест 7")
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.__dict__)
except AttributeError as e:
    print(e)

# TEST_8:
print("\nтест 8")
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    del user.__dict__['_password']
except AttributeError as e:
    print(e)

# TEST_9:
print("\nтест 9")
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

del user.login

try:
    print(user.login)
except AttributeError:
    print('Атрибут отсутствует')

# TEST_10:
print("\nтест 10")
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

user.login = 'Kamiya'
print(user.login)

user.nickname = 'PG'
print(user.nickname)

# TEST_11:
print("\nтест 11")
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user._secret)
except AttributeError as e:
    print(e)

try:
    user._secret = 'PG'
except AttributeError as e:
    print(e)

try:
    del user._secret
except Exception as e:
    print(e)
