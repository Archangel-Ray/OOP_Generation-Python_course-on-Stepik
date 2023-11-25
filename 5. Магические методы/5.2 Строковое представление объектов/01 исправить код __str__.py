"""
Требовалось реализовать класс Book, описывающий книгу.
При создании экземпляра класс должен был принимать три аргумента в следующем порядке:

    title — название книги
    author — автор книги
    year — год выпуска книги

Предполагалось, что экземпляры класса Book будут иметь следующее формальное строковое представление:

Book('<название книги>', '<автор книги>', <год выпуска книги>)

И следующее неформальное строковое представление:

<название книги> (<автор книги>, <год выпуска книги>)

Программист торопился и решил задачу неправильно. Исправьте приведенный ниже код и реализуйте класс Book правильно.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Book нет, она может быть произвольной.
"""


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} ({self.author}, {self.year})'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


# INPUT DATA:

# TEST_1:
book = Book('Изучаем Python', 'Марк Лутц', 2021)

print(book)
print(repr(book))

# TEST_2:
book = Book('Программируем на Python', 'Майкл Доусон', 2023)

print(str(book))
print(repr(book))

# TEST_3:
books = [Book('Программируем на Python', 'Майкл Доусон', 2023),
         Book('Чистый Python', 'Дэн Бейдер', 2022),
         Book('Python. Книга рецептов', 'Бизли и Джонс', 2020)]

print(repr(books))

# TEST_4:
books = [
    Book('Python. К вершинам мастерства', 'Лусиану Рамальо', 2022),
    Book('Лёгкий способо выучить Python', 'Зед Шоу', 2019),
    Book('Изучаем Python', 'Эрик Мэтиз', 2017),
    Book('Python. Экспресс курс', 'Наоми Седер', 2019),
    Book('Pandas. Работа с данными', 'Абдрахманов М.И.', 2020),
    Book('Python и анализ данных', 'Уэс Маккини', 2020),
    Book('Грокаем алгоритмы', 'Адитья Бхаргава', 2017),
]

for book in books:
    print(book.__str__(), book.__repr__(), sep='\n', end='\n\n')
