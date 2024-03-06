"""
Реализуйте класс TypeChecked, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение
    атрибута принадлежит определенному типу данных. При создании экземпляра класс должен принимать произвольное
    количество позиционных аргументов, каждый из которых является типом данных.

Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение
    атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

    Атрибут не найден

При установке или изменении значения атрибута дескриптор должен проверять, принадлежит ли это значение одному из типов,
    указанных при создании дескриптора. Если значение не принадлежит ни одному из типов, должно быть возбуждено
    исключение TypeError с текстом:

    Некорректное значение

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
                используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса TypeChecked нет, она может быть произвольной.
"""


class TypeChecked:
    def __init__(self, *atrs):
        self.possible_attrs = atrs

    def __set_name__(self, cls, name):
        self._name = name

    def __get__(self, obj, cls):
        if obj:
            if self._name in obj.__dict__:
                return obj.__dict__[self._name]
            raise AttributeError("Атрибут не найден")
        return self

    def __set__(self, obj, value):
        if not isinstance(value, self.possible_attrs):
            raise TypeError("Некорректное значение")
        obj.__dict__[self._name] = value


# INPUT DATA:

# TEST_1:
print("\nтест 1")


class Student:
    name = TypeChecked(str)


student = Student()
student.name = 'Mary'

print(student.name)

# TEST_2:
print("\nтест 2")


class Student:
    name = TypeChecked(str)


student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)

# TEST_3:
print("\nтест 3")


class Student:
    name = TypeChecked(str)


student = Student()
student.name = 'Mary'

try:
    student.name = 99
except TypeError as e:
    print(e)

print(student.name)

# TEST_4:
print("\nтест 4")


class Student:
    age = TypeChecked(int, float)


student = Student()

student.age = 18
print(student.age)

student.age = 18.5
print(student.age)

# TEST_5:
print("\nтест 5")


class Vector:
    x = TypeChecked(float)
    y = TypeChecked(float)

    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

    def __str__(self):
        return f'{self.x} {self.y}'


pairs = [('12', '89'), ([1, 2], [3, 4]), ({1: 2}, {3: 4}), (True, False), (1.2, 3.4)]

for x, y in pairs:
    try:
        vector = Vector(x, y)
        print(vector)
    except TypeError as e:
        print(e)

# TEST_6:
print("\nтест 6")


class Student:
    name = TypeChecked(str)


print(Student.name.__class__)
