"""
1. Реализуйте класс данных FootballPlayer, описывающий футбольного игрока. При создании экземпляра класса должен
    принимать три аргумента в следующем порядке:

    name — имя футболиста (тип str)
    surname — фамилия футболиста (тип str)
    value — рыночная стоимость футболиста в евро (тип int)

Экземпляр класса FootballPlayer должен иметь три атрибута:

    name — имя футболиста
    surname — фамилия футболиста
    value — рыночная стоимость футболиста в евро

Также экземпляр класса FootballPlayer должен иметь следующее формальное строковое представление:

FootballPlayer(name='<имя футболиста>', surname='<фамилия футболиста>')

Наконец, экземпляры класса FootballPlayer должны поддерживать между собой все операции сравнения с помощью
    операторов ==, !=, >, <, >=, <=. Два футболиста считаются равными, если их рыночные стоимости совпадают.
    Футболист считается больше другого футболиста, если его рыночная стоимость больше.

2. Реализуйте класс данных FootballTeam, описывающий футбольную команду.
    При создании экземпляра класса должен принимать один аргумент:

    name — название команды (тип str)

Экземпляр класса FootballTeam должен иметь два атрибута:

    name — название команды (тип str)
    players — изначально пустой список, содержащий игроков команды (тип list)

Класс FootballTeam должен иметь один метод экземпляра:

    add_players() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых
                     представляет футболиста, и добавляющий их в команду

Также экземпляр класса FootballTeam должен иметь следующее формальное строковое представление:

FootballTeam(name='<название футбольной команды>')

Наконец, экземпляры класса FootballTeam должны поддерживать между собой операции сравнения с помощью
    операторов == и !=. Две футбольные команды считаются равными, если их названия совпадают.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
              Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
"""
from dataclasses import dataclass, field


@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


@dataclass
class FootballTeam:
    name: str
    players: list = field(repr=False, default_factory=list, compare=False)

    def add_players(self, *args):
        for player in args:
            self.players.append(player)


# INPUT DATA:

print("\n# TEST_1:")
player_ = FootballPlayer('Kylian', 'Mbappe', 180000000)

print(player_)
print(player_.name)
print(player_.surname)
print(player_.value)

print("\n# TEST_2:")
player1 = FootballPlayer('Jude', 'Bellingham', 120000000)
player2 = FootballPlayer('Vinicius', 'Junior', 120000000)
player3 = FootballPlayer('Kylian', 'Mbappe', 180000000)

print(player1 == player2)
print(player1 == player3)
print(player1 > player3)
print(player1 < player3)

print("\n# TEST_3:")
team = FootballTeam('PSG')

print(team)
print(team.name)
print(team.players)

team.add_players(FootballPlayer('Kylian', 'Mbappe', 180000000))
print(team.players)

print("\n# TEST_4:")
team1 = FootballTeam('PSG')
team2 = FootballTeam('PSG')
team3 = FootballTeam('Arsenal')

player1 = FootballPlayer('Jude', 'Bellingham', 120000000)
player2 = FootballPlayer('Vinicius', 'Junior', 110000000)
player3 = FootballPlayer('Kylian', 'Mbappe', 180000000)

team1.add_players(player1)
team2.add_players(player2)
team3.add_players(player3)

print(team1 == team2)
print(team1 != team2)
print(team1 == team3)
print(team1 != team3)

print("\n# TEST_5:")
player1 = FootballPlayer('Ronaldo', '', 20000000)
player2 = FootballPlayer('Lothar', 'Matthaus', 250000000)
player3 = FootballPlayer('Xavi', 'Simons', 54000000)
player4 = FootballPlayer('Paolo', 'Maldini', 28000000)
player5 = FootballPlayer('Лев', 'Яшин', 200000000)
player6 = FootballPlayer('Diego', 'Maradona', 305000000)
player7 = FootballPlayer('Lionel', 'Messi', 180000000)
player8 = FootballPlayer('Kristiano', 'Ronaldo', 10000000)

team = FootballTeam('Best')
print(team.name)

team.add_players(player1, player2, player3, player4, player5, player6, player7, player8)
print(team.players)
