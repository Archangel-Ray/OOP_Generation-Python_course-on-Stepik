"""
Реализуйте класс DefaultObject. При создании экземпляра класс должен принимать один именованный аргумент default,
имеющий значение по умолчанию None, а после произвольное количество именованных аргументов.
Аргументы, передаваемые после default, должны устанавливаться создаваемому экземпляру в качестве атрибутов.

При обращении к несуществующему атрибуту экземпляра класса DefaultObject должно возвращаться значение default.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса DefaultObject нет, она может быть произвольной.
"""


class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        return self.default


# INPUT DATA:

# TEST_1:
print("\nтест 1")
god = DefaultObject(name='Ares', mythology='greek')

print(god.name)
print(god.mythology)
print(god.age)

# TEST_2:
print("\nтест 2")
god = DefaultObject(default=0, name='Tyr', mythology='scandinavian')

print(god.name)
print(god.mythology)
print(god.age)

# TEST_3:
print("\nтест 3")
names = ['Martin', 'Dustin', 'John', 'John Wong', 'John Hanna', 'Theresa', 'Brittany Wheeler', 'David', 'Nancy',
         'Brian Mendez', 'Jennifer Potts', 'Kimberly Walton', 'Debbie Dominguez', 'Marissa Perez', 'Alexander',
         'Shelly', 'Michael', 'Tara', 'Cynthia', 'Jennifer', 'Jesse', 'Douglas', 'Jennifer Patel', 'James', 'Latoya',
         'Kirsten Fisher', 'Brianna', 'Sean', 'Laura', 'Brandi', 'Randall Christian', 'Teresa', 'Keith',
         'Diamond Watson', 'Anne', 'Sarah', 'Earl', 'Kerry Lane', 'Bonnie', 'Dwayne', 'Sonia', 'Mark Miller',
         'Randall Galvan', 'Mark', 'Shannon Stephenson', 'Anthony', 'Steven', 'Samantha Miller', 'Paul Wright',
         'Dennis Lewis', 'Jessica', 'Cody Perry', 'Edward', 'Robert', 'Jacob', 'Adam', 'Tamara', 'Denise Tyler DDS',
         'Angela Jones MD', 'Alexandra', 'Dennis', 'Dawn Clark', 'Kara Mcdonald', 'Anthony Perry', 'Stephanie',
         'Jonathan', 'Amy', 'Martin Collins', 'Joseph', 'Charles Sheppard', 'Shelly Mills', 'Phillip Marshall',
         'Steven Wilson', 'Kimberly Brown', 'Terry Day', 'Mrs. Victoria Dudley', 'Sara', 'Lucas Cooper', 'Brooke',
         'Raymond Gonzalez', 'Randy Moss', 'Lisa', 'Cody Smith', 'Rebecca', 'Nicole Aguilar', 'Jessica Roman',
         'Anna Mcclure MD', 'John Watts', 'Michaela Cochran', 'Penny', 'Randy Keith', 'Alexis Quinn', 'William',
         'Christopher Young', 'Emily Johnson', 'James King', 'Haley', 'Kelly Miller', 'Manuel Lopez', 'Kathleen']

unknown = 'Doe'
for name in names:
    person = name.split()
    if len(person) == 2:
        name, surname = person
        person = DefaultObject(default=unknown, name=name, surname=surname)
    else:
        person = DefaultObject(default=unknown, name=name)
    print(person.name, person.surname)

# TEST_4:
print("\nтест 4")
god = DefaultObject(name='Kratos', mythology='greek')
print('name' in god.__dict__)
print('mythology' in god.__dict__)
