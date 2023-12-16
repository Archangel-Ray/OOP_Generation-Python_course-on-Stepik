"""
Реализуйте функцию hash_function(), которая принимает один аргумент:

    obj — произвольный объект

Функция должна вычислять хеш-значение объекта obj согласно следующему алгоритму:

    1) вычисление значения выражения:

    ord(obj[0]) * ord(obj[-1]) + ord(obj[1]) * ord(obj[-2]) + ord(obj[2]) * ord(obj[-3]) + ...

    где obj — объект, преобразованный в строку с помощью функции str(). Обратите внимание, что суммироваться должны
                произведения первого и последнего элементов, второго и предпоследнего, и так далее до середины.
                Если obj имеет нечетное количество символов, то серединный элемент должен прибавляться без перемножения

    2) вычисление значения выражения:

    ord(obj[0]) * 1 - ord(obj[1]) * 2 + ord(obj[2]) * 3 - ord(obj[3]) * 4 + ...

    где obj — объект, преобразованный в строку с помощью функции str()

    3) вычисление значения выражения:

    (temp1 * temp2) % 123456791

    где temp1 — значение, полученное в первом шаге, temp2 — значение, полученное во втором шаге

и возвращать значение, полученное в третьем шаге.
"""


def hash_function(obj_):
    obj_ = str(obj_)
    len_obj = len(obj_) / 2
    sum_prod_ords = 0
    for i in range(int(len_obj)):
        sum_prod_ords += ord(obj_[i]) * ord(obj_[-(i + 1)])
    if int(str(len_obj).split('.')[1]):
        sum_prod_ords += ord(obj_[int(len_obj)])
    num_difference = ord(obj_[0]) * 1
    for i in range(1, len(obj_), 2):
        num_difference -= ord(obj_[i]) * (i + 1)
        if i + 2 <= len(obj_):
            num_difference += ord(obj_[i + 1]) * (i + 2)
    return (sum_prod_ords * num_difference) % 123456791


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(hash_function('python'))

# TEST_2:
print('\nтест 2')
print(hash_function(12345))

# TEST_3:
print('\nтест 3')
print(hash_function(None))

# TEST_4:
print('\nтест 4')
print(hash_function([1, 2, 3, 'python']))

# TEST_5:
print('\nтест 5')
array = [8022, 530.602391530928, 'lycmfojREEBSKNcNoIjM', False, {'написать': False, 'собеседник': True},
         (1448, True, -3913.85417440914, True),
         [True, True, 554, 'FCLRrFheVhkrubirMUts', -33242154218.4859, 885507704053.121]]

for obj in array:
    print(hash_function(obj))
