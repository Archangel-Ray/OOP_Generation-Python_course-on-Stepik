from contextlib import contextmanager, closing

"""
предназначен для построения контекстных менеджеров из объектов, которые предоставляют метод close(),
    но не реализуют протокол контекстного менеджера (отсутствуют методы __enter__() и __exit__()).
  •	В случае отсутствия метода close() у объекта возбуждается исключение AttributeError.
"""


# Примерный код функции closing():
@contextmanager
def closing_(thing):
    try:
        yield thing
    finally:
        thing.close()


# Использование функции closing():
class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def close(self):
        print('Пока,', self.name)


with closing(Cat('Кемаль')) as cat:  # Метод close() объекта cat будет вызываться всегда,
    print('Привет,', cat)            # даже если в блоке with возникает ошибка.
