"""
Реализуйте класс MutableString, наследника класса UserString, описывающий изменяемую строку. Процесс создания
    экземпляра класса MutableString должен совпадать с процессом создания экземпляра класса UserString.

Класс MutableString должен иметь три метода экземпляра:

    lower() — метод, переводящий все символы изменяемой строки в нижний регистр
    upper() — метод, переводящий все символы изменяемой строки в верхний регистр
    sort() — метод, сортирующий символы изменяемой строки. Может принимать два необязательных именованных
                аргумента key и reverse, выполняющих ту же задачу, что и в функции sorted()

Экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью
    индексов, причем как положительных, так и отрицательных.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса MutableString нет, она может быть произвольной.
"""
from collections import UserString


class MutableString(UserString):
    def __init__(self, string):
        super().__init__(string)
        self.data = string

    def __setitem__(self, index, value):
        _list_ = list(self.data)
        _list_[index] = value
        self.data = "".join(_list_)

    def __delitem__(self, index):
        _list_ = list(self.data)
        del _list_[index]
        self.data = "".join(_list_)

    def upper(self):
        self.data = self.data.upper()

    def lower(self):
        self.data = self.data.lower()

    def sort(self, key=None, reverse=False):
        self.data = "".join(sorted(self.data, key=key, reverse=reverse))


# INPUT DATA:

# TEST_1:
print("\nтест 1")
mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
mutablestring.sort()
print(mutablestring)

# TEST_2:
print("\nтест 2")
mutablestring = MutableString('beegeek')

print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)

# TEST_3:
print("\nтест 3")
words = ['improve', 'north', 'now', 'there', 'outside', 'set', 'into', 'time', 'campaign', 'onto', 'change', 'source',
         'use', 'huge', 'specific', 'consumer', 'speak', 'card', 'century', 'late', 'focus', 'money', 'successful',
         'myself', 'available', 'rise', 'no', 'charge', 'hit', 'friend', 'cost', 'billion', 'financial', 'model',
         'decade', 'whole', 'space', 'service', 'agreement', 'home', 'represent', 'away', 'describe', 'plan', 'drop',
         'dream', 'leg', 'mouth', 'interesting', 'provide', 'indeed', 'thing', 'practice', 'miss', 'bring', 'important',
         'court', 'talk', 'true', 'conference', 'tell', 'issue', 'identify', 'hand', 'appear', 'stuff', 'run',
         'present', 'good', 'region', 'detail', 'recognize', 'international', 'behavior', 'attack', 'politics', 'great',
         'baby', 'measure', 'whether', 'yard', 'with', 'pressure', 'role', 'eight', 'man', 'she', 'four', 'them',
         'adult', 'clear', 'marriage', 'meeting', 'notice']

for word in words:
    mutablestring = MutableString(word)
    print(mutablestring, end=' ')

    mutablestring.upper()
    print(mutablestring, end=' ')

    mutablestring.sort(key=lambda char: ord(char), reverse=True)
    print(mutablestring)

# TEST_4:
print("\nтест 4")
text = '''Spelling: my last name is two words, and I'd like to keep it that way, the spelling on some of my credit
cards notwithstanding. Dutch spelling rules dictate that when used in combination with my first name, "van" is not
capitalized: "Guido van Rossum". But when my last name is used alone to refer to me, it is capitalized, for example:
"As usual, Van Rossum was right."'''

mutablestring = MutableString(text)

mutablestring[208] = 'V'
mutablestring[209] = 'A'
mutablestring[210] = 'N'
print(mutablestring)

# TEST_5:
print("\nтест 5")
text = 'Beautiful is better than ugly.'

mutablestring = MutableString(text)

del mutablestring[9]
print(mutablestring)

del mutablestring[-6]
print(mutablestring)
