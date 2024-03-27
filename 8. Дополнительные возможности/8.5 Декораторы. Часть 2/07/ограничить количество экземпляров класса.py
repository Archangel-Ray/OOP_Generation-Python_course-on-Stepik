"""
Любой пользовательский класс по умолчанию способен создавать бесконечное количество собственных экземпляров.
    Шаблон проектирования синглтон, напротив, гарантирует, что класс имеет только один собственный экземпляр,
    и при попытке создать новый, он возвращает уже имеющийся.

Реализуйте декоратор @limiter для декорирования класса, с помощью которого можно ограничивать количество
    создаваемых декорируемым классом экземпляров до определенного числа. Декоратор должен принимать
    три аргумента в следующем порядке:

    limit — количество экземпляров, которое может создать декорируемый класс
    unique — имя атрибута экземпляра декорируемого класса, значение которого является его идентификатором.
              Два экземпляра с одинаковыми идентификаторами существовать не могут. Если происходит попытка
              создать экземпляр, идентификатор которого совпадает с идентификатором одного из ранее созданных
              экземпляров, должен быть возвращен этот ранее созданный экземпляр
    lookup — определяет, какой объект должен быть возвращен, если превышено ограничение limit, а значение
              атрибута unique ранее не использовалось. При значении FIRST возвращается самый первый созданный
              экземпляр, при значении LAST — самый последний созданный экземпляр

Примечание 1. Гарантируется, что экземпляры декорируемого класса всегда имеют атрибут,
              который содержит их идентификатор.
"""


def limiter(limit, unique, lookup):
    def decorator(cls):
        cls.limit = limit
        cls.instance_dictionary = {}
        cls.first = None
        cls.last = None

        def check(*args, **kwargs):
            instance = cls(*args, **kwargs)
            id_instance = getattr(instance, unique)
            if id_instance in cls.instance_dictionary:
                return cls.instance_dictionary[id_instance]
            if not cls.limit:
                return cls.first if lookup == 'FIRST' else cls.last
            else:
                cls.limit -= 1
                if not cls.first:
                    cls.first = instance
                cls.last = instance
                cls.instance_dictionary[id_instance] = instance
                return instance

        return check

    return decorator


# INPUT DATA:

print("\n# TEST_1:")


@limiter(2, 'ID', 'FIRST')
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value


obj1 = MyClass(1, 5)  # создается экземпляр класса с идентификатором 1
obj2 = MyClass(2, 8)  # создается экземпляр класса с идентификатором 2

obj3 = MyClass(1, 20)  # возвращается obj1, так как экземпляр с идентификатором 1 уже есть
obj4 = MyClass(3, 0)  # превышено ограничение limit, возвращается первый созданный экземпляр

print(obj3.value)
print(obj4.value)

print("\n# TEST_2:")


@limiter(3, 'ID', 'LAST')
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value


obj1 = MyClass(1, 5)  # создается экземпляр класса с идентификатором 1
obj2 = MyClass(2, 8)  # создается экземпляр класса с идентификатором 2
obj3 = MyClass(3, 10)  # создается экземпляр класса с идентификатором 3

obj4 = MyClass(4, 0)  # превышено ограничение limit, возвращается последний созданный экземпляр
obj5 = MyClass(2, 20)  # возвращается obj2, так как экземпляр с идентификатором 2 уже есть

print(obj4.value)
print(obj5.value)

print("\n# TEST_3:")


@limiter(10, 'uniq', 'LAST')
class MyClass:
    def __init__(self, uniq, value):
        self.uniq = uniq
        self.value = value


values = [(0, 48), (1, 17), (2, 36), (3, 26), (4, 52), (5, 90), (6, 98), (7, 46), (8, 86), (9, 95), (10, 35), (11, 84),
          (12, 64), (13, 30), (14, 30), (15, 16), (16, 22), (17, 96), (18, 41), (19, 31)]

for ID, value in values:
    obj = MyClass(ID, value)
    print(f'ID = {obj.uniq}, value = {obj.value}')

print("\n# TEST_4:")


@limiter(10, 'my_id', 'FIRST')
class MyClass:
    def __init__(self, value, my_id):
        self.my_id = my_id
        self.value = value


values = [(84, 0), (97, 1), (41, 2), (80, 3), (31, 4), (40, 5), (26, 6), (51, 7), (68, 8), (41, 9), (76, 10), (56, 11),
          (96, 12), (48, 13), (87, 14), (86, 15), (88, 16), (52, 17), (13, 18), (82, 19)]

for value, ID in values:
    obj = MyClass(value, ID)
    print(f'ID = {obj.my_id}, value = {obj.value}')

print("\n# TEST_5:")


@limiter(12, 'my_id', 'LAST')
class MyClass:
    def __init__(self, value, my_id):
        self.my_id = my_id
        self.value = value


values = [(33, 0), (99, 1), (71, 2), (61, 3), (51, 4), (76, 5), (25, 6), (95, 7), (67, 8), (54, 9), (62, 10), (66, 11),
          (73, 3), (46, 9), (52, 9), (93, 10), (76, 6), (86, 8), (38, 4), (67, 8), (14, 12)]

for value, ID in values:
    obj = MyClass(value, ID)
    print(f'ID = {obj.my_id}, value = {obj.value}')

print("\n# TEST_6:")


@limiter(3, 'my_id', 'LAST')
class MyClass:
    def __init__(self, value, my_id):
        self.my_id = my_id
        self.value = value


obj1 = MyClass(12, 0)
obj2 = MyClass(24, 1)
obj3 = MyClass(36, 2)

obj4 = MyClass(48, 3)
obj5 = MyClass(60, 1)

print(obj4 is obj3)
print(obj5 is obj2)

print("\n# TEST_7:")


@limiter(3, 'my_id', 'FIRST')
class MyClass:
    def __init__(self, value, my_id):
        self.my_id = my_id
        self.value = value


obj1 = MyClass(12, 0)
obj2 = MyClass(24, 1)
obj3 = MyClass(36, 2)

obj4 = MyClass(48, 3)
print(obj4 is obj1)
