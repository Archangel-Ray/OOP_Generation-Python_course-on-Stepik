"""
Реализуйте класс JsonSerializableMixin, добавляющий классам функционал сериализации экземпляров класса в JSON-формат.

Класс JsonSerializableMixin должен иметь один метод экземпляра:

to_json() — метод, возвращающий JSON-представление экземпляра класса
JSON-представлением экземпляра класса должна быть строка формата json, полученная путем сериализации словаря атрибутов
экземпляра класса.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса JsonSerializableMixin нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_8/Module_8.7/Module_8.7.10
"""
import json


class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)


# INPUT DATA:

# TEST_1:
class Empty(JsonSerializableMixin):
    pass


obj = Empty()
print(obj.to_json())


# TEST_2:
class Triangle(JsonSerializableMixin):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


triangle = Triangle(3, 5, 4)
print(triangle.to_json())


# TEST_3:
class Country(JsonSerializableMixin):
    def __init__(self, name, capital, phone_code):
        self.name = name
        self.capital = capital
        self.phone_code = phone_code


country = Country('Russia', 'Moscow', 7)
result = json.loads(country.to_json())
dct = {'name': 'Russia', 'capital': 'Moscow', 'phone_code': 7}
print(isinstance(result, dict))
print(result == dct)


# TEST_4:
class Everything(JsonSerializableMixin):
    def __init__(self):
        self.a = True
        self.b = False
        self.c = [1, True, False, None]
        self.d = (1, True, False, None)
        self.e = {False: True, 1: None}


everything = Everything()
print(everything.to_json())
