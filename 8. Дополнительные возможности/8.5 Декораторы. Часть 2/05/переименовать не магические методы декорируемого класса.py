"""
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_)
    и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.

Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов,
    при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

Частным случаем стиля Camel Case является lower Camel Case, когда с заглавной буквы пишутся все слова, кроме первого.
    Например, beeGeek и helloWorld.

Реализуйте декоратор @snake_case для декорирования класса. Декоратор должен принимать один аргумент:

    attrs — булево значение, по умолчанию равняется False

Декоратор должен переименовать все не магические методы в декорируемом классе, меняя их стиль
    написания c Camel Case и lower Camel Case на Snake Case. Параметр attrs должен определять,
    будут ли аналогичным образом переименованы атрибуты класса. Если он имеет значение True,
    стиль написания имен атрибутов класса должен поменяться с Camel Case и lower Camel Case
    на Snake case, если False — остаться прежним.

Примечание 1. Гарантируется, что имена всех не магических методов и атрибутов в классе написаны в стилях Camel Case,
              lower Camel Case или Snake Case.
"""


def snake_case(attrs=False):
    def to_snake(line):
        new_line = ""
        for letter in line:
            if letter == letter.upper():
                new_line += " "
                new_line += letter.lower()
            else:
                new_line += letter.lower()
        new_line = "_".join(new_line.split())
        if new_line[:2] == "__":
            return new_line[1:]
        else:
            return new_line

    def decorator(cls):
        attrs_name = tuple(cls.__dict__.keys())
        for name in attrs_name:
            if name[:2] != "__":
                if callable(cls.__dict__[name]) or attrs:
                    value_attr = cls.__dict__[name]
                    delattr(cls, name)
                    setattr(cls, to_snake(name), value_attr)

        return cls

    return decorator


# INPUT DATA:

print("\n# TEST_1:")


@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1

    def superSecondMethod(self):
        return 2


obj = MyClass()

print(obj.first_method())
print(obj.super_second_method())

print("\n# TEST_2:")


@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2


print(MyClass.first_attr)
print(MyClass.super_second_attr)

print("\n# TEST_3:")


@snake_case()
class MyClass:
    FirstAttr = 1

    def FirstMethod(self):
        return 1


obj = MyClass()

print(MyClass.FirstAttr)
print(obj.first_method())

print("\n# TEST_4:")


@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2

    def __init__(self):
        self.MyName = 'John Doe'


obj = MyClass()
print(obj.MyName)

myclass_attrs = ['FirstAttr', 'superSecondAttr']

for attr in myclass_attrs:
    try:
        print(MyClass.__dict__[attr])
    except KeyError:
        print('атрибут отсутствует')

print("\n# TEST_5:")


@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1

    def superSecondMethod(self):
        return 2


obj = MyClass()

myclass_attrs = ['FirstMethod', 'superSecondMethod']

for method in myclass_attrs:
    try:
        print(obj.__dict__[method])
    except KeyError:
        print('метод отсутствует')

print("\n# TEST_6:")


@snake_case()
class MyClass:
    def _FirstMethod(self):
        return 1

    def _superSecondMethod(self):
        return 2


obj = MyClass()

print(obj._first_method())
print(obj._super_second_method())
