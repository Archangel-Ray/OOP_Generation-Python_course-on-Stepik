"""
Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Formatter должен иметь один статический метод:

    format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и выводящий
                информацию о переданном объекте в формате, зависящем от его типа. Если переданный объект принадлежит
                какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:

                Аргумент переданного типа не поддерживается

Примечание 1. Примеры форматирования объектов всех типов показаны в тестовых данных.

Примечание 2. Обратите внимание, что метод format() должен обрамлять апострофами строковые элементы коллекций.

Примечание 3. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса Formatter нет, она может быть произвольной.
"""
from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(arg):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @format.register(int)
    @staticmethod
    def format_int(arg):
        print(f"Целое число: {arg}")

    @format.register(float)
    @staticmethod
    def format_float(arg):
        print(f"Вещественное число: {arg}")

    @format.register(list)
    @staticmethod
    def format_list(arg):
        print("Элементы списка: ", end="")
        print(*arg, sep=", ")

    @format.register(tuple)
    @staticmethod
    def format_tuple(arg):
        print("Элементы кортежа: ", end="")
        print(*arg, sep=", ")

    @format.register(dict)
    @staticmethod
    def format_dict(arg):
        print("Пары словаря: ", end="")
        print(*arg.items(), sep=", ")
