"""
Реализуйте неизменяемый класс MusicAlbum, описывающий музыкальный альбом. При создании экземпляра класс должен
    принимать четыре аргумента в следующем порядке:

    title — название альбома (тип str)
    artist — автор альбома (тип str)
    genre — жанр альбома (тип str)
    year — год выпуска альбома (тип int)

Экземпляр класса MusicAlbum должен иметь четыре атрибута:

    title — название альбома
    artist — автор альбома
    genre — жанр альбома
    year — год выпуска альбома

Также экземпляр класса MusicAlbum должен иметь следующее формальное строковое представление:

MusicAlbum(title='<название альбома>', artist='<автор альбома>')

Наконец, экземпляры класса MusicAlbum должны поддерживать между собой операцию сравнения с помощью операторов == и!=.
    Два музыкальных альбома считаются равными, если их названия, авторы и годы выпуска совпадают.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
              Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса MusicAlbum нет, она может быть произвольной.
"""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class MusicAlbum:
    title: str
    artist: str
    genre: str = field(repr=False, compare=False)
    year: int = field(repr=False)


# INPUT DATA:

print("\n# TEST_1:")
print(MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012))

print("\n# TEST_2:")
musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
musicalbum2 = MusicAlbum('Calendar', 'Motorama', 'New Wave, Indie Rock', 2012)

print(musicalbum1 == musicalbum2)
print(musicalbum1 != musicalbum2)

print("\n# TEST_3:")
musicalbum = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)

try:
    musicalbum.genre = 'Post-punk, New Wave, Indie Rock'
except:
    print('Error')

print("\n# TEST_4:")
musicalbum = MusicAlbum('Камнем по голове', 'КиШ', 'Хоррор-панк', 1996)

print(musicalbum.title)
print(musicalbum.artist)
print(musicalbum.genre)
print(musicalbum.year)

print("\n# TEST_5:")
musicalbum = MusicAlbum('Король и Шут', 'КиШ', 'Хоррор-панк', 1997)
print(musicalbum)

print("\n# TEST_6:")
musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
musicalbum2 = MusicAlbum('Calendar', 'Motorama', 'New Wave, Indie Rock', 2013)

print(musicalbum1 == musicalbum2)
print(musicalbum1 != musicalbum2)

print("\n# TEST_7:")
musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
musicalbum2 = MusicAlbum('Poverty', 'Motorama', 'New Wave, Indie Rock', 2012)

print(musicalbum1 == musicalbum2)
print(musicalbum1 != musicalbum2)
