"""
Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.

Класс Processor имеет один статический метод:

    process() — метод, который принимает в качестве аргумента произвольный объект,
                 преобразует его в зависимости от его типа и возвращает полученный результат.
                 Если тип переданного объекта не поддерживается методом,
                 возбуждается исключение TypeError с текстом:

                 Аргумент переданного типа не поддерживается

Перепишите метод process() класса Processor с использованием декоратора @singledispatchmethod,
чтобы он выполнял ту же задачу.

Примечание 1. Примеры преобразования объектов всех поддерживаемых типов показаны в методе process() класса Processor.

Примечание 2. Никаких ограничений касательно реализации класса Processor нет, она может быть произвольной.
"""
from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(float)
    @staticmethod
    def float_process(data):
        return data * 2

    @process.register(int)
    @staticmethod
    def int_process(data):
        return data * 2

    @process.register(str)
    @staticmethod
    def str_process(data):
        return data.upper()

    @process.register(list)
    @staticmethod
    def list_process(data):
        return sorted(data)

    @process.register(tuple)
    @staticmethod
    def tuple_process(data):
        return tuple(sorted(data))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))

# TEST_2:
print('\nтест 2')
try:
    Processor.process({1, 2, 3})
except TypeError as e:
    print(e)

# TEST_3:
print('\nтест 3')
print(Processor.process(100))
print(Processor.process(True))
print(Processor.process(False))
print(Processor.process(55.2))
print(Processor.process('beegeek_stepik_python'))
print(Processor.process((23, 56, 1, 3, -3, 0, 4, 10, 11, -90)))
print(Processor.process([10, 2, 11, 9, 5, -4, -90]))

# TEST_4:
print('\nтест 4')
objects = [None, {1, 2, 3}, {1: 'one', 2: 'two'}]

for obj in objects:
    try:
        Processor.process(obj)
    except TypeError as e:
        print(e)
