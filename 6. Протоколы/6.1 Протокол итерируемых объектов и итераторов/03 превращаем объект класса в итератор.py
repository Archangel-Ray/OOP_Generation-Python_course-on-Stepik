"""
Реализуйте класс AttrsIterator. При создании экземпляра класс должен принимать один аргумент:

    obj — произвольный объект

Экземпляр класса AttrsIterator должен являться итератором, который генерирует все атрибуты объекта obj
    в виде кортежей из двух элементов, первый из которых представляет имя атрибута, второй — значение атрибута.

Примечание 1. Порядок атрибутов при генерации должен совпадать с их порядком в словаре атрибутов __dict__.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс AttrsIterator должен удовлетворять протоколу итератора,
                то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.
"""


class AttrsIterator:
    def __init__(self, obj):
        self.obj = [(key, value) for key, value in obj.__dict__.items()]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.obj:
            raise StopIteration
        return self.obj.pop(0)


# INPUT DATA:

# TEST_1:
print('\nтест 1')


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User('Debbie', 'Harry', 77)
attrsiterator = AttrsIterator(user)

print(*attrsiterator)


# TEST_2:
print('\nтест 2')


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User('Debbie', 'Harry', 77)
user.profession = 'singer'
user.height = 160

attrsiterator = AttrsIterator(user)

print(*attrsiterator, sep='\n')


# TEST_3:
print('\nтест 3')


class Kemal:
    def __init__(self):
        self.family = 'cats'
        self.breed = 'british'
        self.master = 'Kemal'


kemal = Kemal()
attrs_iterator = AttrsIterator(kemal)

print(next(attrs_iterator))
print(next(attrs_iterator))
print(next(attrs_iterator))


# TEST_4:
print('\nтест 4')


class Kish:
    def __init__(self, song, year):
        self.song = song
        self.year = year


forester = Kish('лесник', 1997)
attrs_iterator = AttrsIterator(forester)

next(attrs_iterator)
next(attrs_iterator)

try:
    next(attrs_iterator)
except StopIteration:
    print('Атрибуты закончились')
