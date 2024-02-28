"""
Реализуйте функцию is_context_manager(), которая принимает один аргумент:

    obj — произвольный объект

Функция должна возвращать True, если объект obj является контекстным менеджером, или False в противном случае.
"""
from tempfile import TemporaryFile
from threading import Lock


def is_context_manager(obj):
    return True if '__enter__' in dir(obj) and '__exit__' in dir(obj) else False


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(is_context_manager(open('output.txt', mode='w')))

# TEST_2:
print('\nтест 2')

with TemporaryFile(mode='r+') as file:
    print(is_context_manager(file))

# TEST_3:
print('\nтест 3')

print(is_context_manager(Lock()))

# TEST_4:
print('\nтест 4')
print(is_context_manager(1992))
print(is_context_manager('beegeek'))
print(is_context_manager([1, 2, 3]))
print(is_context_manager({'one': 1, 'two': 2}))
print(is_context_manager(None))

# TEST_5:
print('\nтест 5')


class ContextManager:
    def __enter__(self):
        return 'beegeek'

    def __exit__(self, exc_type, exc_value, exc_tb):
        return True


print(is_context_manager(ContextManager()))

# TEST_6:
print('\nтест 6')


class ContextManager:
    def __init__(self):
        self.inside = False

    def __enter__(self):
        self.inside = True
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.inside = False
        return True


print(is_context_manager(ContextManager()))

# TEST_7:
print('\nтест 7')


class ContextManager:
    def __enter__(self):
        return 'beegeek'


print(is_context_manager(ContextManager()))

# TEST_8:
print('\nтест 8')


class ContextManager:
    def __init__(self):
        self.inside = False

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.inside = False
        return True


print(is_context_manager(ContextManager()))
