from contextlib import contextmanager, nullcontext, suppress

"""
предназеачен для построения пустых контекстных менеджеров, которые ничего не делают.
"""


# Примерный код функции nullcontext():
@contextmanager
def nullcontext_(enter_result=None):
    yield enter_result


# Использование функции nullcontext():
with nullcontext(2077) as manager:
    print(manager)

with nullcontext('pygen') as manager:
    print(manager)


# Функцию nullcontext() удобно использовать для создания необязательного контекстного менеджера
# например:
def my_function(ignore_exceptions=False):
    if ignore_exceptions:
        this_manager = suppress(Exception)  # игнорируем исключения
    else:
        this_manager = nullcontext()  # не игнорируем исключения

    with this_manager:
        pass  # код
