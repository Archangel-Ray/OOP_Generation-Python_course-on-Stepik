"""
Нередко во время сортировки объектов мы используем дополнительную функцию, которая
описывает правило сортировки. Например, если нам нужно отсортировать список экземпляров
некоторого класса на основе значений определенного атрибута, мы можем реализовать функцию,
которая принимает в качестве аргумента этот экземпляр и возвращает значение необходимого атрибута.

Приведенный ниже код:

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]

print(sorted(users, key=lambda user: user.age))

выводит:

[User(Arthur, 20), User(Timur, 30), User(Gvido, 67)]

Удобно было бы иметь класс SortKey, позволяющий сортировать объекты на основе значений различных атрибутов,
лишь перечисляя имена этих атрибутов.

Чтобы приведенный ниже код:

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]

print(sorted(users, key=SortKey('age')))            # сортировка на основе атрибута age
print(sorted(users, key=SortKey('name', 'age')))    # сортировка на основе атрибута name, а затем age

выводил:

[User(Arthur, 20), User(Timur, 30), User(Gvido, 67)]
[User(Arthur, 20), User(Gvido, 67), User(Timur, 30)]

Реализуйте класс SortKey, описывающий ключ для сортировки объектов на основе значений их определенных атрибутов.
При создании экземпляра класс должен принимать произвольное количество позиционных аргументов,
каждый из которых представляет имя атрибута, участвующего в сортировке.

Примечание 1. Имена атрибутов при создании экземпляра класса SortKey передаются в порядке приоритета,
то есть при сортировке сначала должно учитываться значение первого атрибута, затем второго, и так далее.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса SortKey нет, она может быть произвольной.
"""


class SortKey:
    def __init__(self, *args):
        self.args = args

    def __call__(self, obj):
        print('вызов возвращает:', tuple(obj.__dict__[attrib] for attrib in self.args))
        return tuple(obj.__dict__[attrib] for attrib in self.args)


# INPUT DATA:

# TEST_1:
print('\nтест 1')


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(sorted(users, key=SortKey('name')))
print(sorted(users, key=SortKey('name', 'age')))
print(sorted(users, key=SortKey('age')))
print(sorted(users, key=SortKey('age', 'name')))

# TEST_2:
print('\nтест 2')


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(max(users, key=SortKey('name')))
print(max(users, key=SortKey('age')))
print(max(users, key=SortKey('name', 'age')))
print(max(users, key=SortKey('age', 'name')))

# TEST_3:
print('\nтест 3')


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(min(users, key=SortKey('name')))
print(min(users, key=SortKey('age')))
print(min(users, key=SortKey('name', 'age')))
print(min(users, key=SortKey('age', 'name')))

# TEST_4:
print('\nтест 4')


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

users.sort(key=SortKey('name'))
print(users)
users.sort(key=SortKey('name', 'age'))
print(users)
users.sort(key=SortKey('age'))
print(users)
users.sort(key=SortKey('age', 'name'))

# TEST_5:
print('\nтест 5')


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

users.sort(key=SortKey('name'), reverse=True)
print(users)
users.sort(key=SortKey('name', 'age'), reverse=True)
print(users)
users.sort(key=SortKey('age'), reverse=True)
print(users)
users.sort(key=SortKey('age', 'name'), reverse=True)
