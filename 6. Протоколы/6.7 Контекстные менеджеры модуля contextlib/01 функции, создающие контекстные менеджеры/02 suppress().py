from contextlib import contextmanager, suppress

"""
предназначен для построения контекстных менеджеров, которые игнорируют заданные типы исключений.

Как и с любым другим механизмом, который полностью подавляет исключения, этот контекстный менеджер 
    следует использовать только для покрытия специфических ошибок, когда точно известно, 
    что продолжение работы программы без вывода сообщений будет корректным.

  •	Контекстный менеджер, возвращаемый функцией suppress(), является реентерабельным.
"""


# Примерный код функции suppress():
@contextmanager
def suppress_(*exceptions):
    try:
        yield
    except Exception as error:
        if type(error) not in exceptions:
            raise


# Использование функции suppress():
with suppress(ValueError):
    num = int('python')

print('beegeek')

with suppress(TypeError, ZeroDivisionError):
    num = 1 / 0

print('pygen')
