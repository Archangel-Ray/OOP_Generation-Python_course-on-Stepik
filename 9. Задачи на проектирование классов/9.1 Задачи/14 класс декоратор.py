"""
Предикат — это функция, которая возвращает True или False в зависимости от переданных аргументов.

Реализуйте декоратор @predicate, который будет позволять удобно комбинировать предикаты с помощью операторов &, | и ~:

    @predicate
    def is_even(num):
        return num % 2 == 0

    @predicate
    def is_positive(num):
        return num > 0

    print((is_even & is_positive)(4))             # True; равнозначно is_even(4) and is_positive(4)
    print((is_even & is_positive)(3))             # False; равнозначно is_even(3) and is_positive(3)
    print((is_even | is_positive)(3))             # True; равнозначно is_even(3) or is_positive(3)
    print((~is_even & is_positive)(3))            # True; равнозначно not is_even(3) and is_positive(3)

Декоратор должен уметь работать с любыми предикатами, независимо от того, сколько аргументов они принимают:

    @predicate
    def to_be():
        return True

    print((to_be | ~to_be)())                     # True; равнозначно to_be() or not to_be()

    @predicate
    def is_equal(a, b):
        return a == b

    @predicate
    def is_less_than(a, b):
        return a < b

    print((is_less_than | is_equal)(1, 2))        # True; равнозначно is_less_than(1, 2) or is_equal(1, 2)

Также должны поддерживаться как позиционные аргументы, так и именованные:

    print((is_less_than | is_equal)(2, b=2))      # True; равнозначно is_less_than(2, b=2) or is_equal(2, b=2)
    print((is_less_than | is_equal)(a=3, b=2))    # False; равнозначно is_less_than(a=3, b=2) or is_equal(a=3, b=2)

Задекорированная функция должна быть доступна вне комбинаций с другими функциями и вести себя как исходная функция:

    @predicate
    def is_less_than(a, b):
        return a < b

    print(is_less_than(1, 2))                     # True
    print(is_less_than(2, 2))                     # False
    print(is_less_than(3, 2))                     # False

Примечание 1. Гарантируется, что комбинируемые функции имеют одинаковые сигнатуры.
"""


class predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __and__(self, other):
        def wrapper(*args, **kwargs):
            res_self = self(*args, **kwargs)
            res_other = other(*args, **kwargs)
            return res_self and res_other

        return wrapper

    def __or__(self, other):
        def wrapper(*args, **kwargs):
            res_self = self(*args, **kwargs)
            res_other = other(*args, **kwargs)
            return res_self or res_other

        return wrapper

    def __invert__(self):
        def wrapper(*args, **kwargs):
            res = self(*args, **kwargs)
            return not res

        return predicate(wrapper)


# INPUT DATA:

print("\n# TEST_1:")


@predicate
def to_be():
    return True


print((to_be | ~to_be)())  # True; равнозначно to_be() or not to_be()


@predicate
def is_equal(a, b):
    return a == b


@predicate
def is_less_than(a, b):
    return a < b


print((is_less_than | is_equal)(1, 2))  # True; равнозначно is_less_than(1, 2) or is_equal(1, 2)

print((is_less_than | is_equal)(2, b=2))  # True; равнозначно is_less_than(2, b=2) or is_equal(2, b=2)
print((is_less_than | is_equal)(a=3, b=2))  # False; равнозначно is_less_than(a=3, b=2) or is_equal(a=3, b=2)

print("\n# TEST_2:")


@predicate
def is_even(num):
    return num % 2 == 0


@predicate
def is_positive(num):
    return num > 0


print((is_even & is_positive)(4))  # True; равнозначно is_even(4) and is_positive(4)
print((is_even & is_positive)(3))  # False; равнозначно is_even(3) and is_positive(3)
print((is_even | is_positive)(3))  # True; равнозначно is_even(3) or is_positive(3)

print((~is_even & is_positive)(3))  # True; равнозначно not is_even(3) and is_positive(3)

print("\n# TEST_3:")


@predicate
def is_less_than(a, b):
    return a < b


print(is_less_than(1, 2))
print(is_less_than(2, 2))
print(is_less_than(3, 2))

print("\n# TEST_4:")


@predicate
def char_in_word(char, word):
    return char in word


print(char_in_word('e', 'beegeek'))
print((~char_in_word & char_in_word)('e', 'beegeek'))
print((char_in_word | ~char_in_word)(word='beegeek', char='e'))

print("\n# TEST_5:")


@predicate
def is_arithmetic_mean(iterable):
    result = {iterable[i + 1] - iterable[i] for i in range(len(iterable) - 1)}
    return len(result) == 1


@predicate
def is_geometric_mean(iterable):
    result = {iterable[i + 1] // iterable[i] for i in range(len(iterable) - 1)}
    return len(result) == 1


print(is_arithmetic_mean([1, 2, 3, 4, 5]))
print(is_geometric_mean([1, 2, 4, 8, 16]))

print((is_arithmetic_mean & is_geometric_mean)([1, 2, 3, 4, 5]))
print((is_arithmetic_mean | is_geometric_mean)([1, 2, 3, 4, 5]))

print((is_arithmetic_mean & is_geometric_mean)([1, 2, 4, 8, 16]))
print((is_arithmetic_mean | is_geometric_mean)([1, 2, 4, 8, 16]))

print((~is_arithmetic_mean & ~is_geometric_mean)([1, 2, 4, 5]))
print((~is_arithmetic_mean | ~is_geometric_mean)([1, 2, 3, 4, 5]))
