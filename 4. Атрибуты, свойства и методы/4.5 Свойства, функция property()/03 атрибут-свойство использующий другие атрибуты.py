"""
Реализуйте класс Person, описывающий человека.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

    name — имя человека
    surname — фамилия человека

Экземпляр класса Person должен иметь два атрибута:

    name — имя человека
    surname — фамилия человека

Класс Person должен иметь одно свойство:

    fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки:

    <имя> <фамилия>

Примечание 1. При изменении имени и/или фамилии человека должно изменяться и его полное имя.
Аналогично при изменении полного имени должны изменяться имя и фамилия.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return self.name + " " + self.surname

    def set_fullname(self, new):
        self.name, self.surname = new.split()

    fullname = property(get_fullname, set_fullname)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
person = Person('Меган', 'Фокс')

print(person.name)
print(person.surname)
print(person.fullname)

# TEST_2:
print('\nтест 2')
person = Person('Меган', 'Фокс')

person.name = 'Стефани'
print(person.fullname)

# TEST_3:
print('\nтест 3')
person = Person('Алан', 'Тьюринг')

person.surname = 'Вирт'
print(person.fullname)

# TEST_4:
print('\nтест 4')
person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)

# TEST_5:
print('\nтест 5')
person = Person('Брайан', 'Керниган')
print(hasattr(person, 'name'))
print(hasattr(person, 'surname'))
print(hasattr(person, 'fullname'))
