"""
Реализуйте декоратор @auto_repr для декорирования класса. Декоратор должен принимать два аргумента в следующем порядке:

    args — список имен атрибутов
    kwargs — список имен атрибутов

Декоратор должен реализовывать формальное строковое представление для экземпляров декорируемого класса.
    Строковое представление должно содержать имя класса и значения атрибутов экземпляра класса и иметь вид:

    <имя класса>(<атрибут>, <атрибут>, ...)

Если атрибут указан в списке args, в строковом представлении должно быть только его значение, если же атрибут указан
    в списке kwargs, в строковом представлении должно быть его значение вместе с именем.

Примечание 1. Атрибуты в форматированной строке должны располагаться в том порядке,
              в котором они были присвоены экземпляру.

Примечание 2. Гарантируется, что при декорировании указываются все необходимые имена атрибутов. Также гарантируется,
              что имя атрибута указывается либо только в списке args, либо только в списке kwargs. Причем порядок
              расположения имен атрибутов в списках args и kwargs повторяет их расположение в сигнатуре инициализатора
              декорируемого класса.
"""


def auto_repr(args, kwargs):
    def decorator(cls):
        def __repr__(self):
            str_out = []
            for x in (self.__dict__[arg] for arg in args):
                if isinstance(x, str):
                    str_out.append(f"'{x}'")
                else:
                    str_out.append(str(x))
            for kw in kwargs:
                str_out.append(f"{kw}='{self.__dict__[kw]}'")
            return f"{cls.__name__}({', '.join(str_out)})"

        cls.__repr__ = __repr__
        return cls
    return decorator


# INPUT DATA:

print("\n# TEST_1:")


@auto_repr(args=['x', 'y'], kwargs=['color'])
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


point = Point(1, 2, color='green')
print(point)

point.x = 10
point.y = 20
print(point)

print("\n# TEST_2:")


@auto_repr(args=['name', 'surname'], kwargs=[])
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


person = Person('Gvido', 'van Rossum')

print(person)

print("\n# TEST_3:")


@auto_repr(args=[], kwargs=['name', 'breed'])
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


cat = Cat('Кемаль', 'Британский')

print(cat)

print("\n# TEST_4:")


@auto_repr(args=[], kwargs=[])
class Gun:
    pass


gun = Gun()

print(gun)
