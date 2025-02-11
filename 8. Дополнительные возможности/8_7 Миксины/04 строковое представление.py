"""
Реализуйте класс ToStringMixin, добавляющий экземплярам классов следующее формальное и неформальное строковое
    представление:

<имя класса>(<словарь атрибутов экземпляра класса>)

Если экземпляр класса имеет больше 6 атрибутов, словарь атрибутов в формальном и неформальном строковом представлении
    должен иметь следующий формат:

{<атрибут 1>: <значение 1>, <атрибут 2>: <значение 2>, <атрибут 3>: <значение 3>, <атрибут 4>: <значение 4>,
    <атрибут 5>: <значение 5>, <атрибут 6>: <значение 6>, ...}

Примечание 1. Атрибуты в формальном и неформальном строковом представлении должны быть указаны в том же порядке,
              в котором были добавлены в экземпляр.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
              используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса ToStringMixin нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_8/Module_8.7/Module_8.7.13
"""
from itertools import islice


class ToStringMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        list_of_attributes = self.__dict__
        if len(list_of_attributes) > 6:
            list_of_attributes = str(dict(islice(list_of_attributes.items(), 6)))[:-1] + ", ...}"
        return f"{class_name}({list_of_attributes})"


# INPUT DATA:

# TEST_1:
class Empty(ToStringMixin):
    pass


obj = Empty()
print(obj)


# TEST_2:
class Movie(ToStringMixin):
    def __init__(self, title, director, rating):
        self.title = title
        self._director = director
        self.__rating = rating


movie = Movie('Interstellar', 'Christopher Nolan', 8.7)
print(str(movie))
print(repr(movie))


# TEST_3:
class Book(ToStringMixin):
    def __init__(self, title, author, publication_year, genre, pages, language, publisher):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.pages = pages
        self.language = language
        self.publisher = publisher


book = Book('The Hobbit', 'J.R.R. Tolkien', 1937,
            'Fantasy', 310, 'English', 'George Allen & Unwin')
print(book)


# TEST_4:
class Private(ToStringMixin):
    def __init__(self):
        self.__attr1 = None
        self.__attr2 = None


private = Private()
print(str(private))
print(repr(private))


# TEST_5:
class AlmostEmpty(ToStringMixin):
    def __init__(self):
        self.__attribute = None


obj = AlmostEmpty()

for i in range(10):
    obj.__dict__[f'attribute_{i}'] = None
    obj.__dict__[f'_attribute_{i}'] = None

print(str(obj))
print(repr(obj))


# TEST_6:
class MyClass(ToStringMixin):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


obj1 = MyClass()
obj2 = MyClass(a=1, b=2, c=3)
obj3 = MyClass(a=1, b=2, c=3, d=4, e=5, f=6)
obj4 = MyClass(a=1, b=2, c=3, d=4, e=5, f=6, g=7)
print(obj1)
print(obj2)
print(obj3)
print(obj4)
