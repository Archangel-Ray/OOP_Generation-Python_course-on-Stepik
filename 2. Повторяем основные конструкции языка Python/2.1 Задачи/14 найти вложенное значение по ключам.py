# Реализуйте функцию pluck(), которая принимает три аргумента в следующем порядке:
#
#     data — словарь произвольной вложенности
#     path — строка, представляющая собой ключ или последовательность ключей, перечисленных через точку .
#     default — произвольный объект, значение по умолчанию; имеет значение None, если не передан явно
#
# Функция должна возвращать значение по ключу path из словаря data. Если path представляет собой последовательность
# ключей, например, key1.key2, то возвращаемым значением функции должно быть значение по ключу key2
# из словаря data[key1]. Если указанного ключа или хотя бы одного ключа из последовательности ключей в словаре нет,
# функция должна вернуть значение default.


def pluck(data, path, default=None):
    path = path.split('.')
    return_value = None
    if path:
        return_value = data.get(path.pop(0))
    for key in path:
        return_value = return_value.get(key)
    return default if return_value is None else return_value


# INPUT DATA:

# TEST_1:
d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'x'))

# TEST_2:
d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'a.b'))

# TEST_3:
d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

print(pluck(d, 'a.b.c'))

# TEST_4:
d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'c.e'))

# TEST_5:
d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'c'))

# TEST_6:
d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

print(pluck(d, 'a.b.c.d'))

# TEST_7:
d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

print(pluck(d, 'a.b.c.d.e'))

# TEST_8:
d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'c.d'))

# TEST_9:
d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'z', 0))

# TEST_10:
d = {'firstname': 'Тимур', 'lastname': 'Гуев', 'birthdate': {'day': 10, 'month': 'October', 'year': 1993},
     'address': {'streetaddress': 'Часовая 25, кв. 127',
                 'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'},
                 'postalcode': '125315'}}

print(pluck(d, 'birthdate.weekday', default='Not found'))
