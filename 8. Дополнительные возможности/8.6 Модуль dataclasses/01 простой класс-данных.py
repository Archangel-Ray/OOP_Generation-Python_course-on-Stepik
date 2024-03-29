"""
Вам доступен класс City, описывающий город. При создании экземпляра класс принимает три аргумента в следующем порядке:

    name — название города (тип str)
    population — население города (тип int)
    founded — год основания города (тип int)

Экземпляр класса City имеет три атрибута:

    name — название города
    population — население города
    founded — год основания города

Также экземпляр класса City имеет следующее формальное строковое представление:

City(name='<название города>', population=<население города>, founded=<год основания города>)

Наконец, экземпляры класса City поддерживают между собой операцию сравнения с помощью операторов == и !=.
    Два города считаются равными, если их названия, население и годы основания совпадают.

Реализуйте класс City в виде класса данных.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
              Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса City нет, она может быть произвольной.
"""
from dataclasses import dataclass


@dataclass
class City:
    name: str
    population: int
    founded: int


# INPUT DATA:

print("\n# TEST_1:")
city = City('Tokyo', 14043239, 1457)

print(city)
print(city.name)
print(city.population)
print(city.founded)

print("\n# TEST_2:")
city1 = City('Tokyo', 14043239, 1457)
city2 = City('New York', 8467513, 1624)
city3 = City('Tokyo', 14043239, 1457)

print(city1 == city2)
print(city1 != city2)
print(city1 == city3)
print(city1 != city3)

print("\n# TEST_3:")
city = City('Челябинск', 1189525, 1736)

print(city)
print(city.name)
print(city.population)
print(city.founded)

print("\n# TEST_4:")
city = City('Москва', 13015126, 1147)

print(city)
print(city.name)
print(city.population)
print(city.founded)

print("\n# TEST_5:")
city1 = City('Ростов', 1142162, 1749)
city2 = City('Владивосток', 605049, 1860)

print(city1)
print(city1.name)
print(city1.population)
print(city1.founded)

print(city2)
print(city2.name)
print(city2.population)
print(city2.founded)

print(city2 == city2)
print(city1 != city2)
