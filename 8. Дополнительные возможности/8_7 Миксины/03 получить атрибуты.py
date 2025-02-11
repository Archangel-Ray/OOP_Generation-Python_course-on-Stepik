"""
Реализуйте класс AttributesMixin, добавляющий классам функционал получения информации об атрибутах их экземпляров.

Класс AttributesMixin должен иметь два метода экземпляра:

get_public_attributes() — метод, возвращающий список имен и значений публичных атрибутов экземпляров класса,
    которому добавляется функционал.
get_protected_attributes() — метод, возвращающий список имен и значений защищенных атрибутов экземпляров класса,
    которому добавляется функционал.

Списки, возвращаемые методами get_public_attributes() и get_protected_attributes(), должны иметь следующий формат:

[(<имя атрибута>, <значение атрибута>), (<имя атрибута>, <значение атрибута>), ...]

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
              используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса AttributesMixin нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_8/Module_8.7/Module_8.7.12
"""


class AttributesMixin:
    def get_public_attributes(self):
        return [one for one in self.__dict__.items() if one[0][0] != "_"]

    def get_protected_attributes(self):
        return [one for one in self.__dict__.items() if one[0][0] == "_" and "__" not in one[0]]


# INPUT DATA:

# TEST_1:
class Cat(AttributesMixin):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self._breed = breed


cat = Cat('Кемаль', 6, 'Британский')
print(cat.get_public_attributes())
print(cat.get_protected_attributes())


# TEST_2:
class BankAccount(AttributesMixin):
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance


bank_account = BankAccount(245980, 1000)
print(bank_account.get_public_attributes())
print(bank_account.get_protected_attributes())


# TEST_3:
class Order(AttributesMixin):
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self._customer_name = customer_name
        self.__order_details = {}


order = Order(324154, 'Timur')
print(order.get_public_attributes())
print(order.get_protected_attributes())


# TEST_4:
class Empty(AttributesMixin):
    pass


obj = Empty()
print(obj.get_public_attributes())
print(obj.get_protected_attributes())


# TEST_5:
class AlmostEmpty(AttributesMixin):
    def __init__(self):
        self.__attribute = None


obj = AlmostEmpty()

for i in range(10):
    obj.__dict__[f'attribute_{i}'] = None
    obj.__dict__[f'_attribute_{i}'] = None

print(len(obj.get_public_attributes()))
print(len(obj.get_protected_attributes()))


# TEST_6:
class Triangle(AttributesMixin):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


triangle = Triangle(3, 5, 4)
print(triangle.get_public_attributes())
print(triangle.get_protected_attributes())


# TEST_7:
class Private(AttributesMixin):
    def __init__(self):
        self.__attr1 = None
        self.__attr2 = None


private = Private()
print(private.get_public_attributes())
print(private.get_protected_attributes())
