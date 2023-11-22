"""
Реализуйте класс BirthInfo, описывающий данные о дате рождения.
При создании экземпляра класс должен принимать один аргумент:

    birth_date — дата рождения, представленная в одном из следующих вариантов:

    экземпляр класса date
    строка с датой в ISO формате
    список или кортеж из трех целых чисел: года, месяца и дня

Если дата рождения является некорректной или представлена в каком-либо другом формате,
должно быть возбуждено исключение TypeError с текстом:

Аргумент переданного типа не поддерживается

Экземпляр класса BirthInfo должен иметь один атрибут:

    birth_date — дата рождения в виде экземпляра класса date

Класс BirthInfo должен иметь одно свойство:

    age — свойство, доступное только для чтения, возвращающее текущий возраст в годах, то есть количество полных лет,
           прошедших с даты рождения на сегодняшний день

Примечание 1. Возраст в годах должен вычисляться так же, как и обычный возраст человека,
то есть в день рождения его возраст увеличивается на один год.

Примечание 2. Для проверки того, что свойство age возвращает верный возраст, мы используем собственную
функцию current_age(), которая вычисляет возраст в годах на основе даты рождения и текущей даты.

Примечание 3. Никаких ограничений касательно реализации класса BirthInfo нет, она может быть произвольной.
"""
from datetime import date
from functools import singledispatchmethod


class BirthInfo:
    def __init__(self, birth_date):
        self.birth_date = self.birth_date_(birth_date)

    @singledispatchmethod
    def birth_date_(self, arg):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @birth_date_.register(date)
    def birth_date_date(self, arg):
        return arg

    @birth_date_.register(str)
    def birth_date_date(self, arg):
        if arg[0].isdigit() and \
                arg[1].isdigit() and \
                arg[2].isdigit() and \
                arg[3].isdigit() and \
                arg[4] == "-" and \
                arg[5].isdigit() and \
                arg[6].isdigit() and \
                arg[7] == "-" and \
                arg[8].isdigit() and \
                arg[9].isdigit():
            return date.fromisoformat(arg)
        else:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @birth_date_.register(list)
    @birth_date_.register(tuple)
    def birth_date_list(self, arg):
        return date(*arg)

    @property
    def age(self):
        return (date.today() - self.birth_date).days // 365.2
