from contextlib import ExitStack

"""
принимает в качестве аргумента контекстный менеджер, входит в него и добавляет его
    метод __exit__() в конец последовательности обратных вызовов, но не вызывает.

Возвращаемым значением метода enter_context() является возвращаемое значение
    метода __enter__() переданного контекстного менеджера.
"""


class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Привет,', self.name)
        return self.name

    def __exit__(self, *args, **kwargs):
        print('Пока,', self.name)


with ExitStack() as stack:
    name1 = stack.enter_context(Greeter('Гвидо'))
    name2 = stack.enter_context(Greeter('Трей'))
    print(name1, name2)
