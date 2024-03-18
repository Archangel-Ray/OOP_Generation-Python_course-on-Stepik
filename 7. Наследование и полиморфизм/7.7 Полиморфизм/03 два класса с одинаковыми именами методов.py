"""
Будем называть словом любую последовательность из одной или более латинских букв.

1. Реализуйте класс LeftParagraph, описывающий абзац, выровненный по левому краю. При создании экземпляра класс
    должен принимать один аргумент:

    length — длина строки абзаца

Класс LeftParagraph должен иметь два метода экземпляра:

    add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом,
            и добавляющий их в текущий абзац. Если слово не помещается на текущей строке, оно переносится
            на следующую. Также метод должен автоматически добавлять один пробел после каждого добавленного
            слова (кроме последнего)
    end() — метод, печатающий текущий абзац, выровненный по левому краю. После вызова метода текущий абзац
            считается пустым, то есть начинается формирование нового

2. Также реализуйте класс RightParagraph, описывающий абзац, выровненный по правому краю.
    При создании экземпляра класс должен принимать один аргумент:

    length — длина строки абзаца

Класс RightParagraph должен иметь два метода экземпляра:

    add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом,
            и добавляющий их в текущий абзац. Если слово не помещается на текущей строке, оно переносится
            на следующую. Также метод должен автоматически добавлять один пробел после каждого добавленного
            слова (кроме последнего)
    end() — метод, печатающий текущий абзац, выровненный по правому краю с учетом длины строки.
            После вызова метода текущий абзац считается пустым, то есть начинается формирование нового

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
"""


class Paragraph:
    def __init__(self, length):
        self.length = length
        self.paragraph = [[]]

    def add(self, text):
        for word in text.split():
            if len(' '.join(self.paragraph[-1])) + len(word) < self.length:
                self.paragraph[-1].append(word)
            else:
                self.paragraph.append([word])


class LeftParagraph(Paragraph):
    def end(self):
        for row in self.paragraph:
            print(' '.join(row))
        self.paragraph = [[]]


class RightParagraph(Paragraph):
    def end(self):
        for row in self.paragraph:
            print(' '.join(row).rjust(self.length))
        self.paragraph = [[]]


# INPUT DATA:

print("\n# TEST_1:")
leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()

print("\n# TEST_2:")
rightparagraph = RightParagraph(10)

rightparagraph.add('death')
rightparagraph.add('can have me')
rightparagraph.add('when it earns me')
rightparagraph.end()

print("\n# TEST_3:")
leftparagraph = LeftParagraph(23)

leftparagraph.add('Multiply noise and joy')
leftparagraph.add('Sing songs in a good hour')
leftparagraph.add('Friendship grace and youth')
leftparagraph.add('Our birthday girls')
leftparagraph.end()

leftparagraph.add('Meanwhile the winged child')
leftparagraph.add('friends greeting you')
leftparagraph.add('Secretly thinks sometime')
leftparagraph.add('I will be the birthday boy')
leftparagraph.end()

print("\n# TEST_4:")
rightparagraph = RightParagraph(28)

rightparagraph.add('I will not regret the roses')
rightparagraph.add('Withered with a light spring')
rightparagraph.add('I love the grapes on the vines')
rightparagraph.add('Ripened in the hands under the mountain')
rightparagraph.end()

rightparagraph.add('The beauty of my green valley')
rightparagraph.add('Golden joy of autumn')
rightparagraph.add('oblong and transparent')
rightparagraph.add('Like the fingers of a young maiden')
rightparagraph.end()
