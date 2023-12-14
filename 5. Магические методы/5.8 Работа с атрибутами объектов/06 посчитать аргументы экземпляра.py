"""
Реализуйте класс AttrsNumberObject. При создании экземпляра класс должен принимать произвольное количество именованных
    аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Экземпляр класса AttrsNumberObject должен иметь один атрибут:

    attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент,
        включая сам атрибут attrs_num

Примечание 1. Дополнительная проверка данных на корректность не требуется.
    Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса AttrsNumberObject нет, она может быть произвольной.
"""


class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.attrs_num = 1
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __setattr__(self, key, value):
        if key == "attrs_num":
            object.__setattr__(self, key, value)
        else:
            self.attrs_num += 1
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        self.attrs_num -= 1
        del self.__dict__[item]

# INPUT DATA:

# TEST_1:
print("\nтест 1")
music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')

print(music_group.attrs_num)

# TEST_2:
print("\nтест 2")
music_group = AttrsNumberObject()

print(music_group.attrs_num)

# TEST_3:
print("\nтест 3")
music_group = AttrsNumberObject(name='Woodkid', genre='pop')

print(music_group.attrs_num)
music_group.country = 'France'
print(music_group.attrs_num)

# TEST_4:
print("\nтест 4")
music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')

print(music_group.attrs_num)
del music_group.genre
print(music_group.attrs_num)

# TEST_5:
print("\nтест 5")
person = AttrsNumberObject(name='Mark')

print(person.attrs_num)

person.surname = 'Zuckerberg'
print(person.attrs_num)

person.age = 38
print(person.attrs_num)

person.job = 'Programmer'
print(person.attrs_num)
