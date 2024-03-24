"""
1. Реализуйте класс MovieGenres, описывающий флаг с жанрами кино. Флаг должен иметь пять элементов:

    ACTION
    COMEDY
    DRAMA
    FANTASY
    HORROR

2. Также реализуйте класс Movie, описывающий фильм. При создании экземпляра класс должен принимать
    два аргумента в следующем порядке:

    name — название фильма
    genres — жанр фильма (элемент флага MovieGenres)

Класс Movie должен иметь один метод экземпляра:

    in_genre() — метод, принимающий в качестве аргумента жанр и возвращающий True, если фильм принадлежит
                    данному жанру, или False в противном случае

Экземпляр класса Movie должен иметь следующее неформальное строковое представление:

<название фильма>

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
"""
from enum import Flag, auto


class MovieGenres(Flag):
    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()


class Movie:
    def __init__(self, name, genres):
        self.name = name
        self.genres = genres

    def in_genre(self, genre):
        return genre in self.genres

    def __str__(self):
        return self.name


# INPUT DATA:

print("\n# TEST_1:")
movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)

print(movie)

print("\n# TEST_2:")
movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)

print(movie.in_genre(MovieGenres.FANTASY))
print(movie.in_genre(MovieGenres.COMEDY))
print(movie.in_genre(MovieGenres.ACTION | MovieGenres.FANTASY))

print("\n# TEST_3:")
movie = Movie('Scary movie', MovieGenres.COMEDY | MovieGenres.HORROR)

print(movie.in_genre(MovieGenres.FANTASY))
print(movie.in_genre(MovieGenres.COMEDY))
print(movie.in_genre(MovieGenres.COMEDY | MovieGenres.HORROR))

print("\n# TEST_4:")
movie = Movie('Avengers', MovieGenres.FANTASY | MovieGenres.ACTION)

print(movie.in_genre(MovieGenres.DRAMA))
print(movie.in_genre(MovieGenres.ACTION))
print(movie.in_genre(MovieGenres.FANTASY | MovieGenres.ACTION))
print(movie)

print("\n# TEST_5:")
movie = Movie('Любовь и голуби', MovieGenres.DRAMA | MovieGenres.COMEDY)

print(movie.in_genre(MovieGenres.DRAMA))
print(movie.in_genre(MovieGenres.ACTION))
print(movie.in_genre(MovieGenres.DRAMA | MovieGenres.COMEDY))
print(movie)
