"""
Реализуйте класс Versioned, описывающий дескриптор, предоставляющий доступ как к текущему значению атрибута,
    так и ко всем предыдущим, если значение атрибута когда-либо изменялось. При создании экземпляра класс не должен
    принимать никаких аргументов.

Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено.
    Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

    Атрибут не найден

При установке или изменении значения атрибута дескриптор должен устанавливать или изменять это значение
    без каких-либо дополнительных проверок.

Класс Versioned должен иметь два метода экземпляра:

    get_version() — метод, принимающий два аргумента: экземпляр класса, в котором определен дескриптор,
                    и целое число n. Метод должен возвращать n-ое по счету значение атрибута этого экземпляра
                    класса. Например, если значение атрибута было установлено, а затем изменено, то метод
                    get_version() должен уметь вернуть как установленное значение (первое по счету),
                    так и измененное (второе по счету)
    set_version() — метод, принимающий два аргумента: экземпляр класса, в котором определен дескриптор,
                    и целое число n. Метод должен устанавливать n-ое по счету значение атрибута в качестве текущего

Примечание 1. Вызов метода set_version() не должен приравниваться к изменению значения атрибута.
                Будем считать, что атрибут изменяет свое значение только в том случае, если эта
                операция выполняется через точечную нотацию или функцию setattr().

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется,
                что реализованный класс используется только с корректными данными.
"""


class Versioned:
    def __set_name__(self, cls, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj:
            if self._attr in obj.__dict__:
                return obj.__dict__[self._attr]
            raise AttributeError("Атрибут не найден")
        return self

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value
        obj.__dict__.setdefault("list_attrs", list()).append(value)

    @staticmethod
    def get_version(obj, n):
        return obj.list_attrs[n - 1]

    def set_version(self, obj, n):
        obj.__dict__[self._attr] = obj.list_attrs[n - 1]


# INPUT DATA:

# TEST_1:
print("\nтест 1")


class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19

print(student.age)

# TEST_2:
print("\nтест 2")


class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)
print(Student.age.get_version(student, 1))
print(Student.age.get_version(student, 2))
print(Student.age.get_version(student, 3))

# TEST_3:
print("\nтест 3")


class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)
Student.age.set_version(student, 1)
print(student.age)

# TEST_4:
print("\nтест 4")


class Student:
    name = Versioned()


student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)

# TEST_5:
print("\nтест 5")


class Person:
    age = Versioned()


person = Person()

person.age = 0
for _ in range(50):
    person.age += 1

for i in range(51):
    print(Person.age.get_version(person, i + 1))

# TEST_6:
print("\nтест 6")


class Person:
    age = Versioned()


person = Person()

person.age = 0
for _ in range(50):
    person.age += 1

print(person.age)
Person.age.set_version(person, 32)
print(person.age)

# TEST_7:
print("\nтест 7")


class Student:
    age = Versioned()


student1 = Student()
student2 = Student()

student1.age = 18
student1.age = 19
student1.age = 20

student2.age = 30
student2.age = 31
student2.age = 32

print(student1.age)
print(student2.age)
Student.age.set_version(student1, 1)
Student.age.set_version(student2, 2)
print(student1.age)
print(student2.age)

# TEST_8:
print("\nтест 8")


class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)

Student.age.set_version(student, 1)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))

Student.age.set_version(student, 2)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))

# TEST_9:
print("\nтест 9")


class Student:
    age = Versioned()


print(Student.age.__class__)
