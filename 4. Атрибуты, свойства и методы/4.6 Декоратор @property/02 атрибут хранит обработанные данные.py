"""
В целях безопасности в базах данных пароли от аккаунтов пользователей хранятся не в явном виде,
а в виде хеш-значений — чисел, вычисленных по специальному алгоритму на основе паролей.

Вам доступна функция hash_function(), которая принимает в качестве аргумента пароль и возвращает его хеш-значение.

Реализуйте класс Account, описывающий аккаунт интернет-пользователя на некотором сервисе.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

    login — логин пользователя
    password — пароль пользователя

Класс Account должен иметь два свойства:

    login — свойство, доступное только для чтения, возвращающее логин пользователя.
             При попытке изменения свойства должно быть возбуждено исключение AttributeError с текстом:

             Изменение логина невозможно

    password — свойство, доступное для чтения и записи, возвращающее хеш-значение пароля от аккаунта пользователя.
                При изменении свойство должно вычислять хеш-значение нового пароля и сохранять его, а не сам пароль

Примечание 1. Дополнительная проверка данных на корректность не требуется.
              Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Account нет, она может быть произвольной.
"""


class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        raise AttributeError('Изменение логина невозможно')

    def get_password(self):
        return self._password

    def set_password(self, new_pass):
        self._password = self.hash_function(new_pass)

    password = property(get_password, set_password)

    @staticmethod
    def hash_function(password_):
        hash_value = 0
        for char, index in zip(password_, range(len(password_))):
            hash_value += ord(char) * index
        return hash_value % 10 ** 9


# INPUT DATA:

# TEST_1:
print('\nтест 1')
account = Account('hannymad', 'cakeisalie')

print(account.login)
print(account.password)

# TEST_2:
print('\nтест 2')
account = Account('timyr-guev', 'lovebeegeek')

print(account.password)
account.password = 'verylovebeegeek'
print(account.password)

# TEST_3:
print('\nтест 3')
account = Account('timyr-guev', 'lovebeegeek')
try:
    account.login = 'timyrik30'
except AttributeError as e:
    print(e)

# TEST_4:
print('\nтест 4')
account = Account('svvaliv', 'no_one_will_know_my_password')
try:
    account.login = 'vzohan'
except AttributeError as e:
    print(e)

# TEST_5:
print('\nтест 5')
account = Account('gvido', 'van_rossum')

print(hasattr(account, 'login'))
print(hasattr(account, 'password'))
