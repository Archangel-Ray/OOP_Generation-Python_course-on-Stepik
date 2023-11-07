# Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Гарантируется, что возвращаемое значение функции принадлежит типу, который поддерживается форматом JSON.

import json


def jsonify(func):
    def wrapper(*args, **kwargs):
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return json.dumps(func(*args, **kwargs))
    return wrapper


# INPUT DATA:

# TEST_1:
@jsonify
def make_user(id_, live, options):
    return {'id': id_, 'live': live, 'options': options}


print(make_user(4, False, None))


# TEST_2:
@jsonify
def make_list(n):
    return list(range(1, n + 1))


print(make_list(10))


# TEST_3:
@jsonify
def make_str(s1, s2):
    return (s1 + s2) * 5


print(make_str('bee', 'geek'))


# TEST_4:
@jsonify
def make_square(num):
    return num ** 2


print(make_square(10))
print(make_square(10.5))


# TEST_5:
@jsonify
def make_bool(flag):
    return not flag


print(make_bool(True))
print(make_bool(False))


# TEST_6:
@jsonify
def make_none():
    return None


print(make_none())


# TEST_7:
@jsonify
def make_tuple():
    """JSON-Tuple object"""
    return 1, '2', 3.0, None, False, {'1': True}


print(make_tuple())
print(make_tuple.__name__)
print(make_tuple.__doc__)
