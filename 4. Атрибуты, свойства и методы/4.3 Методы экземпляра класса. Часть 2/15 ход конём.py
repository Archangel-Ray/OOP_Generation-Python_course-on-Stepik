"""
Реализуйте класс Knight, описывающий шахматного коня.
При создании экземпляра класс должен принимать три аргумента в следующем порядке:

    horizontal — координата коня по горизонтальной оси, представленная латинской буквой от a до h
    vertical — координата коня по вертикальной оси, представленная целым числом от 1 до 8 включительно
    color — цвет коня (black или white)

Экземпляр класса Knight должен иметь три атрибута:

    horizontal — координата коня на шахматной доске по горизонтальной оси
    vertical — координата коня на шахматной доске по вертикальной оси
    color — цвет коня

Класс Knight должен иметь четыре метода экземпляра:

    get_char() — метод, возвращающий символ N
    can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям и
    возвращающий True, если конь может переместиться на клетку с данными координатами, или False в противном случае
    move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям и
    заменяющий текущие координаты коня на переданные. Если конь из текущей клетки не может переместиться на клетку с
    указанными координатами, его координаты должны остаться неизменными
    draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может
    переместиться конь. Пустые клетки должны быть отображены символом ., конь — символом N, клетки,
    на которые может переместиться конь, — символом *
"""


class Knight:
    horizontal_coords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.horizontal_in = self.horizontal_coords.index(horizontal)
        self.vertical_in = 8 - vertical
        self.list_possible_moves = []
        self.possible_moves()
        self.color = color

    @staticmethod
    def get_char():
        return "N"

    def possible_moves(self):
        new_list_moves = []
        for v, h in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
            if 0 <= self.vertical_in + v < 8 and 0 <= self.horizontal_in + h < 8:
                new_list_moves.append((self.vertical_in + v, self.horizontal_in + h))
        self.list_possible_moves = new_list_moves

    def can_move(self, horizontal, vertical):
        return (8 - vertical, self.horizontal_coords.index(horizontal)) in self.list_possible_moves

    def move_to(self, horizontal, vertical):
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical
            self.horizontal_in = self.horizontal_coords.index(horizontal)
            self.vertical_in = 8 - vertical
            self.possible_moves()

    def draw_board(self):
        chess_board = [['.' for _ in range(8)] for _ in range(8)]
        chess_board[self.vertical_in][self.horizontal_in] = self.get_char()
        for x, y in self.list_possible_moves:
            chess_board[x][y] = "*"
        for row in chess_board:
            print(*row, sep="")


# INPUT DATA:

print('TEST_1:')
knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)

print('TEST_2:')
knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)

print('TEST_3:')
knight = Knight('c', 3, 'white')

knight.draw_board()

print('TEST_4:')
knight = Knight('e', 5, 'black')

knight.draw_board()
knight.move_to('d', 3)
print()
knight.draw_board()

print('TEST_5:')
knight = Knight('a', 1, 'white')

knight.draw_board()
knight.move_to('e', 8)
print()
knight.draw_board()

print('TEST_6:')
knight = Knight('g', 7, 'black')
knight.draw_board()

print('TEST_7:')
knight = Knight('d', 8, 'white')
knight.draw_board()

print('TEST_8:')
knight = Knight('h', 1, 'black')
knight.draw_board()
