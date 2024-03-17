"""
С помощью множественного наследования постройте иерархию из приведенных ниже четырех классов.
    При решении старайтесь свести дублирование кода к минимуму.

1. Реализуйте класс Father, описывающий отца.
    При создании экземпляра класс должен принимать один аргумент:

    mood — настроение, по умолчанию равняется строке neutral

Экземпляр класса Father должен иметь один атрибут:

    mood — настроение

Класс Father должен иметь два метода экземпляра:

    greet() — метод, возвращающий строку Hello!
    be_strict() — метод, изменяющий значение атрибута mood на строку strict

2. Также реализуйте класс Mother, описывающий мать.
    При создании экземпляра класс должен принимать один аргумент:

    mood — настроение, по умолчанию равняется строке neutral

Экземпляр класса Mother должен иметь один атрибут:

    mood — настроение

Класс Mother должен иметь два метода экземпляра:

    greet() — метод, возвращающий строку Hi, honey!
    be_kind() — метод, изменяющий значение атрибута mood на строку kind

3. Помимо этого, реализуйте класс Daughter, описывающий дочь.
    При создании экземпляра класс должен принимать один аргумент:

    mood — настроение, по умолчанию равняется строке neutral

Экземпляр класса Daughter должен иметь один атрибут:

    mood — настроение

Класс Daughter должен иметь три метода экземпляра:

    greet() — метод, возвращающий строку Hi, honey!
    be_kind() — метод, изменяющий значение атрибута mood на строку kind
    be_strict() — метод, изменяющий значение атрибута mood на строку strict

4. Наконец, реализуйте класс Son, описывающий сына.
    При создании экземпляра класс должен принимать один аргумент:

    mood — настроение, по умолчанию равняется строке neutral

Экземпляр класса Son должен иметь один атрибут:

    mood — настроение

Класс Son должен иметь три метода экземпляра:

    greet() — метод, возвращающий строку Hello!
    be_kind() — метод, изменяющий значение атрибута mood на строку kind
    be_strict() — метод, изменяющий значение атрибута mood на строку strict

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
"""
from abc import ABC, abstractmethod


class Family(ABC):
    def __init__(self, mood="neutral"):
        self.mood = mood

    @staticmethod
    @abstractmethod
    def greet():
        pass


class Father(Family):
    @staticmethod
    def greet():
        return "Hello!"

    def be_strict(self):
        self.mood = "strict"


class Mother(Family):
    @staticmethod
    def greet():
        return "Hi, honey!"

    def be_kind(self):
        self.mood = "kind"


class Daughter(Mother, Father):
    pass


class Son(Father, Mother):
    pass


# INPUT DATA:

print("\n# TEST_1:")
father = Father()
mother = Mother()

print(father.mood)
print(mother.mood)
print(father.greet())
print(mother.greet())

print("\n# TEST_2:")
father = Father('happy')
mother = Mother('unhappy')

print(father.mood)
print(mother.mood)
father.be_strict()
mother.be_kind()
print(father.mood)
print(mother.mood)

print("\n# TEST_3:")
daughter = Daughter()

print(daughter.greet())
print(daughter.mood)
daughter.be_kind()
print(daughter.mood)
daughter.be_strict()
print(daughter.mood)

print("\n# TEST_4:")
son = Son()

print(son.greet())
print(son.mood)
son.be_kind()
print(son.mood)
son.be_strict()
print(son.mood)
