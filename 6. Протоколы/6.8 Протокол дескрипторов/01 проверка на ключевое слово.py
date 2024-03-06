"""
Реализуйте класс NonKeyword, описывающий дескриптор, который проверяет, что устанавливаемое
    или изменяемое значение атрибута не является строковым ключевым словом в Python.
    При создании экземпляра класс должен принимать один аргумент:

    name — имя атрибута, за которым будет закреплен дескриптор

При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено.
    Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

    Атрибут не найден

При установке или изменении значения атрибута дескриптор должен проверять, не является ли это значение
    строковым ключевым словом в Python. Если значение является строковым ключевым словом, должно быть
    возбуждено исключение ValueError с текстом:

    Некорректное значение

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса NonKeyword нет, она может быть произвольной.
"""
from keyword import kwlist


class NonKeyword:
    def __init__(self, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj:
            if self._attr not in obj.__dict__:
                raise AttributeError("Атрибут не найден")
            return obj.__dict__[self._attr]
        return self

    def __set__(self, obj, value):
        if value in kwlist:
            raise ValueError("Некорректное значение")
        obj.__dict__[self._attr] = value


# INPUT DATA:

# TEST_1:
print("\nтест 1")


class Student:
    name = NonKeyword('name')


student = Student()
student.name = 'Peter'

print(student.name)

# TEST_2:
print("\nтест 2")


class Student:
    name = NonKeyword('name')


student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)

# TEST_3:
print("\nтест 3")


class Student:
    name = NonKeyword('name')


student = Student()
student.name = 'Peter'

try:
    student.name = 'class'
except ValueError as e:
    print(e)

# TEST_4:
print("\nтест 4")


class Student:
    name = NonKeyword('name')


student = Student()

try:
    student.name = 'class'
except ValueError as e:
    print(e)

# TEST_5:
print("\nтест 5")


class Student:
    name = NonKeyword('name')


student = Student()

for kw in kwlist:
    try:
        student.name = kw
    except ValueError as e:
        print(e)

# TEST_6:
print("\nтест 6")


class NonKeywordData:
    obj = NonKeyword('obj')


data = [1, 2.3, [4, 5, 6], (7, 8, 9), {10: 11, 12: 13, 14: 15}, True, False, 'Mantrida']
nonkeyworddata = NonKeywordData()

for item_ in data:
    nonkeyworddata.obj = item_
    print(nonkeyworddata.obj)

# TEST_7:
print("\nтест 7")


class Student:
    name = NonKeyword('name')


print(Student.name.__class__)
