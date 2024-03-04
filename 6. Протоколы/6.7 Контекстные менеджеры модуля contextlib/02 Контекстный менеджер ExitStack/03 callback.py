from contextlib import ExitStack

"""
принимает в качестве аргумента функцию, любой набор из позиционных или именованных аргументов для этой функции, 
    и добавляет эту функцию в конец последовательности обратных вызовов, но не вызывает.
"""


def goodbye(name):
    print('Пока,', name)


with ExitStack() as stack:
    stack.callback(goodbye, 'Гвидо')
    stack.callback(goodbye, name='Трей')
    print('Завершение блока with')
