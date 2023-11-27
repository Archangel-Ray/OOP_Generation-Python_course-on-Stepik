"""
Реализуйте класс ReversibleString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:

    string — значение строки

Экземпляр класса ReversibleString должен иметь следующее неформальное строковое представление:

<значение строки>

Также экземпляр класса ReversibleString должен поддерживать унарный оператор -,
результатом которого должен являться новый экземпляр класса ReversibleString со значением строки в обратном порядке.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса ReversibleString нет, она может быть произвольной.
"""


class ReversibleString:
    def __init__(self, string_):
        self.string = string_

    def __str__(self):
        return self.string

    def __neg__(self):
        return ReversibleString(self.string[::-1])


# INPUT DATA:

# TEST_1:
print('\nтест 1')
string = ReversibleString('python')

print(string)
print(-string)

# TEST_2:
print('\nтест 2')
string = ReversibleString('p')

print(string)
print(-string)

# TEST_3:
print('\nтест 3')
string = ReversibleString('')

print(string)
print(-string)

# TEST_4:
print('\nтест 4')
string = ReversibleString("Namespaces are one honking great idea -- let's do more of those!")

print(string)
print(-string)

# TEST_5:
print('\nтест 5')
string = ReversibleString('beegeek')

print(-string)
print(type(-string))

# TEST_6:
print('\nтест 6')
strings = [ReversibleString('social'), ReversibleString('history'), ReversibleString('certain'),
           ReversibleString('end'), ReversibleString('wear'), ReversibleString('into'), ReversibleString('PM'),
           ReversibleString('factor'), ReversibleString('budget'), ReversibleString('I'), ReversibleString('know'),
           ReversibleString('statement'), ReversibleString('similar'), ReversibleString('do'), ReversibleString('with'),
           ReversibleString('voice'), ReversibleString('fact'), ReversibleString('already'),
           ReversibleString('quality'), ReversibleString('growth'), ReversibleString('television'),
           ReversibleString('during'), ReversibleString('direction'), ReversibleString('fact'),
           ReversibleString('system'), ReversibleString('floor'), ReversibleString('production'),
           ReversibleString('dog'), ReversibleString('image'), ReversibleString('price'), ReversibleString('while'),
           ReversibleString('conference'), ReversibleString('though'), ReversibleString('white'),
           ReversibleString('statement'), ReversibleString('view'), ReversibleString('fight'), ReversibleString('plan'),
           ReversibleString('third'), ReversibleString('minute'), ReversibleString('rate'), ReversibleString('with'),
           ReversibleString('soldier'), ReversibleString('book'), ReversibleString('whose'), ReversibleString('decade'),
           ReversibleString('only'), ReversibleString('ago'), ReversibleString('study'), ReversibleString('at'),
           ReversibleString('message'), ReversibleString('first'), ReversibleString('challenge'),
           ReversibleString('more'), ReversibleString('paper'), ReversibleString('senior'),
           ReversibleString('practice'), ReversibleString('wrong'), ReversibleString('edge'),
           ReversibleString('knowledge'), ReversibleString('person'), ReversibleString('much'),
           ReversibleString('race'), ReversibleString('piece'), ReversibleString('management'),
           ReversibleString('pass'), ReversibleString('vote'), ReversibleString('performance'),
           ReversibleString('brother'), ReversibleString('sister'), ReversibleString('apple'),
           ReversibleString('early'), ReversibleString('while'), ReversibleString('director'),
           ReversibleString('consumer'), ReversibleString('city'), ReversibleString('reason'), ReversibleString('boy'),
           ReversibleString('off'), ReversibleString('trip'), ReversibleString('action'), ReversibleString('physical'),
           ReversibleString('always'), ReversibleString('myself'), ReversibleString('despite'),
           ReversibleString('early'), ReversibleString('a'), ReversibleString('bill'), ReversibleString('part'),
           ReversibleString('even'), ReversibleString('summer'), ReversibleString('behavior'),
           ReversibleString('attorney'), ReversibleString('artist'), ReversibleString('project'),
           ReversibleString('test'), ReversibleString('win'), ReversibleString('and'), ReversibleString('character'),
           ReversibleString('particularly')]

for string in strings:
    print(-string)
