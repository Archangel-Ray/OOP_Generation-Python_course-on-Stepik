"""
Реализуйте класс User, описывающий интернет-пользователя.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

    name — имя пользователя. Если name не является непустой строкой, состоящей только из букв,
            должно быть возбуждено исключение ValueError с текстом:

    Некорректное имя

    age — возраст пользователя. Если age не является целым числом, принадлежащим отрезку [0; 110],
           должно быть возбуждено исключение ValueError с текстом:

    Некорректный возраст

Экземпляр класса User должен иметь два атрибута:

    _name — имя пользователя
    _age — возраст пользователя

Класс User должен иметь четыре метода экземпляра:

    get_name() — метод, возвращающий имя пользователя
    set_name() — метод, принимающий в качестве аргумента значение new_name и изменяющий имя пользователя на new_name.
                  Если new_name не является непустой строкой, состоящей только из букв,
                  должно быть возбуждено исключение ValueError с текстом:

    Некорректное имя

    get_age() — метод, возвращающий возраст пользователя
    set_age() — метод, принимающий в качестве аргумента значение new_age и изменяющий возраст пользователя на new_age.
                 Если new_age не является целым числом, принадлежащим отрезку [0; 110],
                 должно быть возбуждено исключение ValueError с текстом:

    Некорректный возраст

Примечание 1. Если при создании экземпляра класса User имя и возраст одновременно являются некорректными,
должно быть возбуждено исключение, связанное с именем.
"""


class User:
    def __init__(self, name_, age_):
        self._name = None
        self.set_name(name_)
        self._age = None
        self.set_age(age_)

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if type(new_name) is str and new_name and new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError('Некорректное имя')

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if type(new_age) is int and 0 < new_age < 110:
            self._age = new_age
        else:
            raise ValueError('Некорректный возраст')


# INPUT DATA:

# TEST_1:
print('\nTEST 1:')
user = User('Гвидо', 67)

print(user.get_name())
print(user.get_age())

# TEST_2:
print('\nTEST 2:')
user = User('Гвидо', 67)

user.set_name('Тимур')
user.set_age(30)

print(user.get_name())
print(user.get_age())

# TEST_3:
print('\nTEST 3:')
user = User('Меган', 37)

invalid_names = (-1, True, '', [], '123456', 'Меган906090')

for name in invalid_names:
    try:
        user.set_name(name)
    except ValueError as e:
        print(e)

# TEST_4:
print('\nTEST 4:')
user = User('Меган', 37)

invalid_ages = ('ten', [], '', [True], -1, 111, 136, -50, 18.5)
for age in invalid_ages:
    try:
        user.set_age(age)
    except ValueError as e:
        print(e)

# TEST_5:
print('\nTEST 5:')
invalid_names = (-1, True, '', [], '123456', 'Меган906090')

for name in invalid_names:
    try:
        user = User(name, 37)
    except ValueError as e:
        print(e)

# TEST_6:
print('\nTEST 6:')
invalid_ages = ('ten', [], '', [True], -1, 111, 136, -50)
for age in invalid_ages:
    try:
        user = User('Меган', age)
    except ValueError as e:
        print(e)

# TEST_7:
print('\nTEST 7:')
try:
    user = User('Gvido_1956', '67')
except ValueError as e:
    print(e)
