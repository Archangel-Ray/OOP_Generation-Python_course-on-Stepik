"""
Предположим, что у нас имеется некоторая игра. За каждую игровую сессию игрок получает определенное количество
    баллов в зависимости от своего результата. Вашей задачей является реализация класса HighScoreTable — таблицы
    рекордов, которую можно будет обновлять с учетом итоговых результатов игрока.

Изначально таблица рекордов является пустой. Максимальное количество рекордов указывается при создании таблицы:

    high_score_table = HighScoreTable(3)

Таблица должна позволять просматривать текущие рекорды и добавлять новые результаты:

    print(high_score_table.scores)    # []
    high_score_table.update(10)
    high_score_table.update(8)
    high_score_table.update(12)
    print(high_score_table.scores)    # [12, 10, 8]

Текущие рекорды всегда должны располагаться в порядке убывания. Так как таблица содержит именно рекорды,
    то после заполнения таблицы добавляться должны только те результаты, которые лучше текущих:

    high_score_table.update(6)
    high_score_table.update(7)
    print(high_score_table.scores)    # [12, 10, 8]
    high_score_table.update(9)
    print(high_score_table.scores)    # [12, 10, 9]

Таблица должна поддерживать сброс всех результатов:

    high_score_table.reset()
    print(high_score_table.scores)    # []
"""


class HighScoreTable:
    def __init__(self, max_len):
        self.scores = []
        self.max_len = max_len

    def update(self, arg):
        self.scores.append(arg)
        self.scores.sort(reverse=True)
        self.scores = self.scores[:self.max_len]

    def reset(self):
        self.scores.clear()

    def __repr__(self):
        return repr(self.scores)


# INPUT DATA:

print("\n# TEST_1:")
high_score_table = HighScoreTable(3)

print(high_score_table.scores)
high_score_table.update(10)
high_score_table.update(8)
high_score_table.update(12)
print(high_score_table.scores)

print("\n# TEST_2:")
high_score_table = HighScoreTable(3)

print(high_score_table.scores)
high_score_table.update(10)
high_score_table.update(8)
high_score_table.update(12)
print(high_score_table.scores)

high_score_table.update(3)
high_score_table.update(6)
high_score_table.update(1)
print(high_score_table.scores)

high_score_table.reset()
print(high_score_table.scores)

print("\n# TEST_3:")
high_score_table = HighScoreTable(3)

print(high_score_table.scores)
high_score_table.update(10)
high_score_table.update(8)
high_score_table.update(12)
print(high_score_table.scores)

high_score_table.update(18)
high_score_table.update(11)
high_score_table.update(13)
print(high_score_table.scores)

print("\n# TEST_4:")
high_score_table = HighScoreTable(5)

print(high_score_table.scores)

scores = [34, 30, 66, 28, 17, 97, 75, 24, 24, 81, 19, 38, 57, 45, 52, 67, 13, 32, 86, 99, 21, 18, 13, 70, 88, 84, 54,
          15, 71, 33, 75, 36, 56, 85, 59, 88, 57, 24, 34, 51, 29, 54, 92, 22, 70, 49, 86, 77, 10, 40, 77, 28, 50, 44,
          73, 28, 16, 90, 94, 17, 65, 93, 68, 77, 84, 18, 12, 86, 74, 29, 38, 12, 28, 24, 41, 54, 53, 35, 11, 80, 95,
          10, 93, 42, 23, 57, 81, 20, 78, 73, 51, 19, 55, 71, 45, 62, 54, 42, 39, 54]

for score in scores:
    high_score_table.update(score)

print(high_score_table.scores)

print("\n# TEST_5:")
high_score_table = HighScoreTable(20)

print(high_score_table.scores)

scores = [74, 95, 57, 69, 26, 75, 34, 32, 78, 15, 42, 41, 62, 17, 31, 87, 90, 69, 47, 28, 26, 64, 71, 65, 41, 39, 59,
          29, 83, 12, 11, 72, 51, 34, 50, 36, 29, 36, 70, 84, 52, 98, 46, 24, 85, 35, 98, 10, 64, 84, 99, 53, 47, 99,
          41, 19, 67, 33, 36, 74, 20, 86, 91, 18, 55, 47, 71, 71, 82, 38, 32, 78, 51, 53, 46, 99, 44, 90, 59, 94, 75,
          71, 39, 97, 67, 52, 90, 19, 26, 48, 22, 18, 21, 41, 97, 35, 78, 63, 50, 91, 19, 23, 77, 47, 26, 17, 16, 45,
          93, 13, 22, 30, 78, 87, 42, 73, 26, 65, 55, 64, 54, 26, 67, 93, 88, 46, 14, 99, 41, 98, 71, 62, 75, 87, 93,
          43, 47, 69, 65, 40, 33, 40, 32, 98, 31, 97, 21, 10, 75, 16, 97, 17, 31, 98, 60, 96, 90, 47, 91, 35, 15, 20,
          59, 25, 87, 39, 51, 23, 81, 62, 94, 10, 74, 32, 14, 18, 11, 50, 25, 100, 26, 58, 62, 81, 80, 34, 77, 23, 60,
          89, 74, 34, 12, 100, 77, 82, 34, 13, 43, 40, 66, 49, 29, 84, 62, 37, 51, 84, 93, 55, 67, 78, 17, 50, 70, 45,
          69, 86, 97, 28, 14, 85, 40, 53, 45, 66, 93, 15, 10, 12, 61, 93, 76, 16, 93, 70, 89, 85, 44, 60, 74, 27, 41,
          25, 18, 34, 98, 16, 88, 51, 91, 34, 14, 41, 53, 21, 62, 27, 54, 35, 37, 32, 96, 21, 78, 71, 58, 13, 75, 75,
          44, 72, 99, 92, 20, 77, 83, 56, 59, 85, 73, 94, 63, 88, 56, 100, 52, 61, 34, 53, 33, 32, 45, 69, 88, 84, 82,
          63, 35, 94, 20, 51, 94, 51, 69, 11, 22, 40, 79, 45, 82, 64, 84, 24, 50, 84, 46, 72, 36, 66, 58, 74, 13, 98,
          46, 26, 79, 36, 64, 59, 98, 27, 73, 37, 48, 31, 67, 74, 17, 75, 17, 19, 35, 12, 93, 87, 21, 57, 36, 37, 39,
          37, 69, 83, 81, 33, 42, 48, 44, 87, 48, 38, 50, 45, 94, 84, 83, 45, 12, 20, 29, 50, 27, 96, 45, 91, 18, 51,
          13, 45, 25, 30, 85, 93, 71, 90, 84, 74, 88, 81, 96, 67, 25, 40, 68, 73, 80, 76, 15, 36, 49, 15, 68, 40, 86,
          68, 73, 48, 38, 86, 23, 98, 79, 62, 84, 16, 14, 11, 74, 21, 77, 14, 73, 99, 21, 48, 83, 51, 53, 66, 55, 27,
          14, 38, 47, 45, 88, 52, 43, 73, 56, 74, 45, 98, 65, 61, 37, 69, 87, 92, 57, 61, 13, 68, 94, 15, 88, 30, 26,
          51, 99, 53, 19, 13, 20, 34, 67, 48, 94, 38, 95, 35, 78, 60, 13, 100, 26, 36, 20, 97, 64, 68, 62, 55, 51, 39,
          55, 33, 70, 87, 17, 33, 32, 82, 50, 53, 43, 35, 38, 47, 10, 71, 12, 78, 87, 85, 13, 25, 66, 40, 22, 67, 63,
          57, 72, 70, 89, 23, 92, 49, 29, 48, 91, 70, 39, 83, 20, 18, 78, 36, 53, 57, 78, 87, 68, 10, 12, 78, 22, 90,
          82, 14, 67, 63, 21, 13, 66, 48, 77, 18, 39, 30, 84, 40, 78, 98, 15, 100, 49, 37, 75, 39, 69, 72, 75, 47, 79,
          90, 95, 33, 89, 52, 33, 100, 66, 44, 46, 69, 54, 76, 81, 40, 30, 60, 92, 13, 92, 92, 54, 80, 53, 36, 99, 12,
          30, 68, 64, 15, 85, 76, 81, 35, 27, 65, 64, 24, 69, 99, 99, 16, 29, 32, 73, 83, 26, 78, 13, 87, 39, 81, 13,
          71, 60, 53, 34, 54, 59, 54, 58, 97, 12, 93, 92, 73, 37, 46, 67, 61, 48, 86, 27, 31, 44, 16, 16, 33, 52, 62,
          43, 81, 69, 23, 13, 67, 17, 38, 69, 21, 28, 66, 55, 52, 99, 12, 17, 48, 75, 71, 36, 79, 71, 21, 70, 84, 34,
          32, 99, 73, 87, 99, 34, 84, 93, 83, 16, 73, 53, 59, 67, 69, 46, 20, 13, 42, 58, 22, 17, 48, 95, 82, 11, 39,
          41, 48, 65, 42, 54, 65, 42, 56, 93, 97, 33, 40, 72, 79, 43, 61, 48, 21, 37, 35, 50, 40, 32, 21, 56, 22, 46,
          92, 12, 92, 15, 54, 90, 74, 88, 80, 30, 55, 56, 64, 33, 13, 37, 74, 96, 18, 14, 79, 69, 17, 46, 36, 68, 56,
          90, 57, 50, 86, 81, 55, 60, 81, 28, 53, 97, 85, 85, 72, 59, 64, 20, 35, 86, 62, 55, 68, 18, 11, 17, 81, 43,
          86, 78, 39, 48, 71, 45, 87, 30, 96, 91, 23, 13, 41, 79, 68, 41, 80, 35, 15, 99, 75, 86, 82, 68, 57, 56, 61,
          32, 57, 24, 80, 88, 35, 99, 60, 49, 41, 10, 75, 46, 67, 80, 56, 53, 79, 30, 50, 21, 54, 44, 78, 47, 34, 77,
          19, 47, 82, 32, 67, 82, 77, 34, 65, 65, 50, 83, 37, 12, 46, 73, 70, 22, 94, 33, 83, 31, 72, 52, 65, 13, 21,
          29, 59, 52, 53, 89, 69, 38, 58, 29, 91, 56, 41, 53, 51, 76, 38, 93, 90, 22, 70, 68, 69, 38, 20, 22, 83, 31,
          75, 68, 88, 80, 97, 88, 49, 14, 47, 99, 34, 67, 82, 99, 98, 19, 72, 26, 72, 82, 72, 32, 45, 46, 61, 99, 21,
          51, 45, 14, 34, 99, 63, 57, 97, 78, 25, 17, 18, 33, 77, 31, 46, 85, 29, 94, 97, 100, 48, 64, 70, 44, 40, 100,
          31, 25, 48, 11, 65, 85, 70, 77, 36, 99, 83, 70, 64, 99, 45, 92, 71, 29, 89, 36, 32, 26, 85, 54, 13, 75, 67,
          64, 55, 44, 47, 78, 93, 49, 84, 35, 66, 11, 44, 40, 13, 75, 96, 31, 92, 10, 29, 62, 50, 46, 79, 100, 50, 91,
          90]

for score in scores:
    high_score_table.update(score)

print(high_score_table.scores)
