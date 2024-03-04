from contextlib import ExitStack

"""
принимает в качестве аргумента контекстный менеджер и добавляет его метод __exit__() в конец последовательности 
    обратных вызовов, но не вызывает. Не выполняет вход в переданный контекстный менеджер.
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
    stack.push(Greeter('Гвидо'))
    stack.push(Greeter('Трей'))
    print('Завершение блока with')
