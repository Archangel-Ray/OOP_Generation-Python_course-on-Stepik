"""
Реализуйте функцию limited_hash(), которая принимает три аргумента в следующем порядке:

    left — целое число
    right — целое число
    hash_function — хеш-функция, по умолчанию равняется встроенной функции hash()

Функция должна возвращать новую функцию, которая принимает в качестве аргумента произвольный объект, вычисляет его
хеш-значение с помощью функции hash_function(), преобразует его в число, принадлежащее диапазону [left; right],
и возвращает полученный результат.

Если вычисленное хеш-значение уже принадлежит диапазону [left; right], то функция должна возвращать его без
преобразования. Если вычисленное хеш-значение равняется right + 1, то функция перед возвратом должна преобразовать его
в left, если right + 2 — в left + 1, если right + 3 — в left + 2, и так далее. Аналогичные преобразования,
но в другую сторону, должны выполняться для хеш-значений, которые меньше left. Преобразования должны выполняться
циклично при очередном выходе из диапазона.
"""


def limited_hash(left, right, hash_function=hash):
    residual = right - left + 1

    def wrapper(arg):
        result = hash_function(arg)
        while right < result:
            result -= residual
        while result < left:
            result += residual
        return result
    return wrapper


# INPUT DATA:

# TEST_1:
print('\nтест 1')


hash_function = limited_hash(10, 15)

print(hash_function(10))
print(hash_function(11))
print(hash_function(15))

# TEST_2:
print('\nтест 2')


hash_function = limited_hash(10, 15)

print(hash_function(16))
print(hash_function(17))
print(hash_function(21))
print(hash_function(22))
print(hash_function(23))

# TEST_3:
print('\nтест 3')


hash_function = limited_hash(10, 15)

print(hash_function(9))
print(hash_function(8))
print(hash_function(4))
print(hash_function(3))
print(hash_function(2))

# TEST_4:
print('\nтест 4')


hash_function = limited_hash(2, 3, hash_function=lambda obj: len(str(obj)))

print(hash_function('a'))
print(hash_function('ab'))
print(hash_function('abc'))
print(hash_function('abcd'))
print(hash_function('abcde'))
print(hash_function('abcdef'))
print(hash_function('abcdefg'))

# TEST_5:
print('\nтест 5')


def hash_function(obj):
    return sum(index * ord(character) for index, character in enumerate(str(obj), start=1))


hash_function = limited_hash(10, 15, hash_function)

array = [1366, -5502567186.7395, 'zZQyrjYzdgcabTZPATPl', False, {'монета': -671699723096.267, 'лететь': 5151},
         (False, True, 897, -844416.51017117, 1101),
         [True, 171664.794743347, True, False, 'UypAaBSjBWYWBYbmRTdN', 4044844490314.56]]

for item in array:
    print(hash_function(item))
