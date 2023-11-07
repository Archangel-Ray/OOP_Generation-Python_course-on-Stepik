# Реализуйте декоратор @recviz, который полностью визуализирует выполнение декорируемой функции,
# в том числе и рекурсивной. Декоратор должен отображать все рекурсивные вызовы и возвращаемые значения,
# полученные при этих вызовах, причем рекурсивные вызовы, выполняемые в глубину,
# должны отделяться друг от друга четырьмя пробелами.
#
# Очередной вызов декорируемой функции при визуализации должен включать в себя знак ->,
# имя декорируемой функции и аргументы, переданные при этом вызове. Возвращаемое значение при визуализации
# должно включать в себя знак <- и непосредственно само возвращаемое значение.
#
# Примечание 1. Рекурсивный вызов и возвращаемое значение, полученное при этом вызове,
# должны находиться на одном уровне отступов.
#
# Примечание 2. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

from functools import lru_cache, wraps


def recviz(func):
    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        list_args = list(map(lambda x: "'" + str(x) + "'" if type(x) is str else str(x), args))
        list_kwargs = []
        for key, value in kwargs.items():
            string = f"{key}="
            if type(value) in (int, float) or type(value) is bool:
                string += str(value)
            else:
                string += "'" + value + "'"
            list_kwargs.append(string)
        print('    ' * count, '-> ', func.__name__, '(', ', '.join(list_args + list_kwargs), ')', sep='')
        count += 1
        res = func(*args, **kwargs)
        count -= 1
        res_out = res
        if type(res) is str:
            res_out = "'" + res + "'"
        print('    ' * count, '<- ', res_out, sep='')
        return res
    return wrapper


# INPUT DATA:

# TEST_1:
@recviz
def add(a, b):
    return a + b


add(1, b=2)
print()


# TEST_2:
@recviz
def add(a, b, c, d, e):
    return (a + b + c) * (d + e)


add('a', b='b', c='c', d=3, e=True)
print()


# TEST_3:
@recviz
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(4)
print()


# TEST_4:
@recviz
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


fact(5)
print()


# TEST_5:
@lru_cache
@recviz
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(7)
print()


# TEST_6:
@recviz
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(7)
