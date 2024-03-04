from contextlib import ExitStack

"""
немедленно опустошает последовательность обратных вызовов, 
    вызывая с конца все имеющиеся в нем методы __exit__() и функции.
"""


class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Привет,', self.name)
        return self.name

    def __exit__(self, *args, **kwargs):
        print('Пока,', self.name)


def goodbye(name):
    print('Пока,', name)


with ExitStack() as stack:
    stack.enter_context(Greeter('Гвидо'))
    stack.push(Greeter('Трей'))
    stack.callback(goodbye, 'Алан')
    stack.close()
    print('Завершение блока with')
