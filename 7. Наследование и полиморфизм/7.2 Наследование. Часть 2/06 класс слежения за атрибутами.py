"""
Реализуйте класс FieldTracker, наследники которого получают возможность отслеживать состояние определенных атрибутов
    своих экземпляров класса. Дочерние классы должны наследовать четыре метода экземпляра:

    base() — метод, принимающий в качестве аргумента имя атрибута и возвращающий либо текущее значение этого атрибута,
              либо исходное (указанное при определении) значение этого атрибута, если оно было изменено
    has_changed() — метод, принимающий в качестве аргумента имя атрибута и возвращающий True, если значение этого
                     атрибута было изменено хотя бы раз, или False в противном случае
    changed() — метод, возвращающий словарь, в котором ключами являются имена атрибутов, которые изменяли свои
                 значения, а значениями — их исходные значения
    save() — метод, сбрасывающий отслеживание. После вызова метода считается, что все атрибуты ранее не изменяли
              свои значения, а их текущие значения считаются исходными

Гарантируется, что наследники класса FieldTracker:

    всегда имеют атрибут класса fields, содержащий кортеж с атрибутами, которые необходимо отслеживать
    в своем инициализаторе всегда вызывают инициализатор класса FieldTracker после установки первичных значений
        отслеживаемым атрибутам

Примечание 1. Будем считать, что атрибут изменяет свое значение только в том случае,
                если устанавливаемое значение отличается от текущего.

Примечание 2. Реализация класса FieldTracker может быть произвольной, то есть требований к наличию определенных
                атрибутов нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.
"""


class FieldTracker:
    fields = tuple()

    def __init__(self):
        self.cache = dict()
        self.save()

    def base(self, name):
        if name in self.fields:
            return self.cache[name]

    def has_changed(self, name):
        return self.cache[name] != self.__dict__[name]

    def changed(self):
        return {n: v for n, v in self.cache.items() if self.has_changed(n)}

    def save(self):
        for name in self.fields:
            self.cache[name] = self.__dict__[name]


# INPUT DATA:

# TEST_1:
print("\nтест 1")


class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


point = Point(1, 2, 3)

print(point.base('x'))
print(point.has_changed('x'))
print(point.changed())

# TEST_2:
print("\nтест 2")


class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.z = 5

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())

# TEST_3:
print("\nтест 3")


class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.save()

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())

# TEST_4:
print("\nтест 4")


class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.changed())
p.x = 4
print(p.changed())
print(p.x)
p.z = 6
print(p.changed())
p.save()
print(p.changed())
p.y = 8
print(p.changed())
print(p.y)
p.save()
print(p.changed())
p.save()
print(p.changed())

# TEST_5:
print("\nтест 5")


class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.x = 4
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.z = 6
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.save()
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.y = 8
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.save()
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))

# TEST_6:
print("\nтест 6")


class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.base('x'))
p.x = 4
print(p.base('x'))
print(p.x)
p.z = 6
print(p.base('x'))
print(p.base('y'))
print(p.base('z'))
p.save()
print(p.base('x'))
print(p.base('y'))
print(p.base('z'))
p.y = 8
print(p.base('y'))
print(p.y)
p.save()
print(p.base('y'))
