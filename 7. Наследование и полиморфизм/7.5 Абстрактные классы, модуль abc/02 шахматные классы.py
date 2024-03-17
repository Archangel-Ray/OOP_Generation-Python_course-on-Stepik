"""
1. Реализуйте абстрактный класс ChessPiece, описывающий шахматную фигуру. Инициализатор класса должен принимать
    два аргумента в следующем порядке:

    horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
    vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно

    Класс ChessPiece должен иметь один метод экземпляра:

    can_move() — пустой абстрактный метод

2. Также реализуйте класс King, наследника класса ChessPiece, описывающий шахматного короля.
    Процесс создания экземпляра класса King должен совпадать с процессом создания экземпляра класса ChessPiece.

    Класс King должен иметь один метод экземпляра:

    can_move() — метод, принимающий в качестве аргументов шахматные координаты по горизонтали
                    и вертикали и возвращающий True, если фигура может переместиться по указанным
                    координатам, или False в противном случае

    Экземпляр класса King  должен иметь два атрибута:

    horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
    vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно

3. Наконец, реализуйте класс Knight, наследника класса ChessPiece, описывающий шахматного коня.
    Процесс создания экземпляра класса Knight должен совпадать с процессом создания экземпляра класса ChessPiece.

    Класс Knight должен иметь один метод экземпляра:

    can_move() — переопределенный родительский метод, принимающий в качестве аргументов координаты
                    по горизонтали и вертикали и возвращающий True, если фигура может переместиться
                    по указанным координатам, и False в противном случае

    Экземпляр класса Knight  должен иметь два атрибута:

    horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
    vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно

Примечание 1. Шахматная доска имеет вид:

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованные классы используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализаций классов нет, она может быть произвольной.
"""
from abc import ABC


class ChessPiece(ABC):
    horizontal_coords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def __init__(self, horizontal, vertical, of_the_piece=()):
        self.horizontal = horizontal
        self.vertical = vertical
        self.of_the_piece = of_the_piece
        self.list_possible_moves = self.possible_moves(of_the_piece)

    def possible_moves(self, list_possible_moves):
        new_list_moves = []
        for v, h in list_possible_moves:
            if 0 <= 8 - self.vertical + v < 8 and 0 <= self.horizontal_coords.index(self.horizontal) + h < 8:
                new_list_moves.append((8 - self.vertical + v, self.horizontal_coords.index(self.horizontal) + h))
        return new_list_moves

    def can_move(self, horizontal, vertical):
        return (8 - vertical, self.horizontal_coords.index(horizontal)) in self.list_possible_moves


class King(ChessPiece):
    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical,
                         ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)))


class Knight(ChessPiece):
    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical,
                         ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)))


# INPUT DATA:

# TEST_1:
print("\nтест 1")
king = King('b', 2)

print(king.can_move('c', 3))
print(king.can_move('a', 1))
print(king.can_move('f', 7))

# TEST_2:
print("\nтест 2")
knight = Knight('c', 3)

print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

# TEST_3:
print("\nтест 3")
king = King('e', 3)

print(king.can_move('e', 3))
print(king.can_move('e', 4))
print(king.can_move('b', 1))

# TEST_4:
print("\nтест 4")
knight = Knight('h', 8)

print(knight.can_move('h', 8))
print(knight.can_move('a', 6))
print(knight.can_move('a', 1))
print(knight.can_move('g', 6))

# TEST_5:
print("\nтест 5")
knight = Knight('a', 1)

for horizontal_ in 'abcdefg':
    for vertical_ in range(1, 9):
        print(f'{horizontal_}{vertical_}', knight.can_move(horizontal_, vertical_))

# TEST_6:
print("\nтест 6")
king = King('a', 1)

for horizontal_ in 'abcdefg':
    for vertical_ in range(1, 9):
        print(f'{horizontal_}{vertical_}', king.can_move(horizontal_, vertical_))

# TEST_7:
print("\nтест 7")
kings = [King(h, v) for h in 'abcdefgh' for v in range(1, 9)]

for king in kings:
    print('*' * 20)
    for horizontal_ in 'abcdefgh':
        for vertical_ in range(1, 9):
            if king.can_move(horizontal_, vertical_):
                print(f'King({king.horizontal}{king.vertical})', f'{horizontal_}{vertical_}',
                      king.can_move(horizontal_, vertical_))

# TEST_8:
print("\nтест 8")
knights = [Knight(h, v) for h in 'abcdefgh' for v in range(1, 9)]

for knight in knights:
    print('*' * 20)
    for horizontal_ in 'abcdefgh':
        for vertical_ in range(1, 9):
            if knight.can_move(horizontal_, vertical_):
                print(f'Knight({knight.horizontal}{knight.vertical})', f'{horizontal_}{vertical_}',
                      knight.can_move(horizontal_, vertical_))
