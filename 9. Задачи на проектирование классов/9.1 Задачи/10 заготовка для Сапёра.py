"""
В этой задаче вам необходимо реализовать поле для игры в Сапера в виде двух классов Game и Cell. Экземпляр первого
    класса будет описывать само игровое поле, экземпляр класса Cell — одну его ячейку. Экземпляр класса Game должен
    создаваться на основе трех значений: количество строк (длина поля), количество столбцов (ширина поля) и общее
    количество мин на поле:

    game = Game(14, 18, 40)    # 14 строк, 18 столбцов и 40 мин

Количество строк и столбцов, а также общее количество мин должны быть доступны по соответствующим атрибутам:

    print(game.rows)           # 14
    print(game.cols)           # 18
    print(game.mines)          # 40

Также экземпляр класса Game должен иметь атрибут board, представляющий игровое поле в виде двумерного списка.
    Количество подсписков в этом списке должно совпадать с количеством строк, количество элементов
    в подсписках — с количеством столбцов. Каждый элемент подсписка должен представлять собой экземпляр
    класса Cell и иметь соответствующий набор атрибутов:

    cell = game.board[0][0]

    print(cell.row)            # 0; строка ячейки
    print(cell.col)            # 0; столбец ячейки
    print(cell.mine)           # True или False в зависимости от того, содержит ячейка мину или нет
    print(cell.neighbours)     # число от 0 до 8, количество мин в соседних ячейках

Игровое поле при создании должно заполняться минами случайным образом.

Примечание 1. Для проверки того, что в экземпляре класса Cell хранится верное количество мин в соседних ячейках, в
              одном из тестов мы используем собственную функцию get_neighbours_count(), которая считает это количество.
"""
from random import randrange


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mine = False
        self.neighbours = 0


class Game:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = self.lay_mines()

    def lay_mines(self):
        board = [[Cell(x, y) for y in range(self.cols)] for x in range(self.rows)]
        for _ in range(self.mines):
            while True:
                x, y = randrange(self.rows), randrange(self.cols)
                if not board[x][y].mine:
                    board[x][y].mine = True
                    break
        for row in board:
            for cell in row:
                if not cell.mine:
                    for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        x_row, y_col = cell.row + x, cell.col + y
                        if 0 <= x_row < self.rows and 0 <= y_col < self.cols and board[x_row][y_col].mine:
                            cell.neighbours += 1
        return board


# INPUT DATA:

print("\n# TEST_1:")
game = Game(14, 18, 40)
print(game.rows)
print(game.cols)
print(game.mines)

cell_ = game.board[0][0]

print(cell_.row)
print(cell_.col)
print(0 <= cell_.neighbours <= 3)

print("\n# TEST_2:")
game = Game(10, 8, 14)

for r, c in ((0, 0), (0, -1), (-1, 0), (-1, -1)):
    cell_ = game.board[r][c]
    print(0 <= cell_.neighbours <= 3, type(cell_))

print("\n# TEST_3:")
game = Game(10, 8, 14)

for r in (0, -1):
    for c in range(1, game.cols - 1):
        cell_ = game.board[r][c]
        print(0 <= cell_.neighbours <= 5, type(cell_))

print("\n# TEST_4:")
game = Game(10, 8, 14)

for c in (0, -1):
    for r in range(1, game.rows - 1):
        cell_ = game.board[r][c]
        print(0 <= cell_.neighbours <= 5, type(cell_))

# print("\n# TEST_5:")
# n, m = 10, 8
# game = Game(n, m, 14)
# total_mines = 0
#
# for r in range(n):
#     for c in range(m):
#         if not game.board[r][c].mine:
#             print(get_neighbours_count(r, c, game) == game.board[r][c].neighbours)
#         total_mines += game.board[r][c].mine
#
# print(total_mines == game.mines)
# print(total_mines)
# print(game.mines)
