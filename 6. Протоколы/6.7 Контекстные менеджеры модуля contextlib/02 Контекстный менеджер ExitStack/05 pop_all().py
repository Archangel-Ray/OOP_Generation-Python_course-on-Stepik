from contextlib import ExitStack

"""
переносит последовательность обратных вызовов в новый контекстный менеджер ExitStack и возвращает его. 
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
    stack.enter_context(Greeter('Гвидо'))
    stack.enter_context(Greeter('Трей'))
    stack.enter_context(Greeter('Алан'))
    new_stack = stack.pop_all()
    print('Завершение блока with')

print('\nПосле завершения первого блока with закрываем сохранённый')
new_stack.close()
