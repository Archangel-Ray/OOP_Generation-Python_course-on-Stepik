"""
Реализуйте класс TicTacToe для игры в Крестики-Нолики. Экземпляр класса TicTacToe должен представлять собой игровое
    поле из трех строк и трех столбцов, на котором игроки по очереди могут помечать свободные клетки.
    Первый ход делает игрок, ставящий крестики:

    tictactoe = TicTacToe()

    tictactoe.mark(1, 1)         # помечаем крестиком клетку с координатами (1; 1)
    tictactoe.mark(3, 1)         # помечаем ноликом клетку с координатами (3; 1)

Помечать уже помеченные клетки нельзя. При попытке сделать это должен быть выведен текст Недоступная клетка:

    tictactoe.mark(1, 1)         # Недоступная клетка

    tictactoe.mark(1, 3)         # помечаем крестиком клетку с координатами (1; 3)
    tictactoe.mark(1, 2)         # помечаем ноликом клетку с координатами (1; 2)
    tictactoe.mark(3, 3)         # помечаем крестиком клетку с координатами (3; 3)
    tictactoe.mark(2, 2)         # помечаем ноликом клетку с координатами (2; 2)
    tictactoe.mark(2, 3)         # помечаем крестиком клетку с координатами (2; 3)

С помощью метода winner() должна быть возможность узнать победителя игры. Метод должен вернуть:

    символ X, если победил игрок, ставящий крестики
    символ O, если победил игрок, ставящий нолики
    строку Ничья, если произошла ничья
    значение None, если победитель еще не определен

print(tictactoe.winner())    # X

Помечать клетки после завершения игры нельзя. При попытке сделать это должен быть выведен текст Игра окончена:

tictactoe.mark(2, 1)         # Игра окончена

С помощью метода show() должна быть возможность посмотреть текущее состояние игрового поля. Оно должно быть построено
    из символов | и -, а также X и O, если игроками были сделаны какие-либо ходы. Для приведенного выше поля tictactoe
    вызов tictactoe.show() должен вывести следующее:

X|O|X
-----
 |O|X
-----
O| |X
"""


class TicTacToe:
    def __init__(self):
        self.playing_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.next_player = self.next_player()

    @staticmethod
    def next_player():
        while True:
            for player in "XO":
                yield player

    def mark(self, x, y):
        if self.winner():
            print("Игра окончена")
            return
        if self.playing_field[x - 1][y - 1] == " ":
            self.playing_field[x - 1][y - 1] = next(self.next_player)
        else:
            print("Недоступная клетка")

    def winner(self):
        winning_options = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                           [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                           [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
        for coords in winning_options:
            winning = set()
            for x, y in coords:
                winning.add(self.playing_field[x][y])
            if len(winning) == 1 and winning.pop() != " ":
                return self.playing_field[coords[0][0]][coords[0][1]]
        if " " in "".join("".join(string) for string in self.playing_field):
            return None
        return "Ничья"

    def show(self):
        print(*("|".join(row) for row in self.playing_field), sep="\n-----\n")


# INPUT DATA:

print("\n# TEST_1:")
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 1)
tictactoe.mark(1, 1)

tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.mark(2, 1)
tictactoe.show()

print("\n# TEST_2:")
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 2)
tictactoe.mark(1, 1)

tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.show()

print("\n# TEST_3:")
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 2)
tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)
tictactoe.mark(2, 2)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)

print("\n# TEST_4:")
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(1, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)

print(tictactoe.winner())

tictactoe.mark(3, 2)
tictactoe.mark(3, 3)
tictactoe.mark(1, 2)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)
print(tictactoe.winner())
