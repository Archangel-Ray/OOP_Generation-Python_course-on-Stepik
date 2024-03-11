"""
Реализуйте класс LowerString, наследника класса str, описывающий строку, которая во время создания автоматически
    переводится в нижний регистр. При создании экземпляра класс должен принимать один аргумент:

    obj — объект, определяющий начальное значение строки. Может быть не передан,
            в таком случае начальное значение считается пустой строкой

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса LowerString нет, она может быть произвольной.
"""


class LowerString(str):
    def __new__(cls, obj=""):
        return super().__new__(cls, str(obj).lower())


# INPUT DATA:

# TEST_1:
print("\nтест 1")
s1 = LowerString('BEEGEEK')
s2 = LowerString('BeeGeek')

print(s1)
print(s2)
print(s1 == s2)
print(issubclass(LowerString, str))

# TEST_2:
print("\nтест 2")
print(LowerString(['Bee', 'Geek']))
print(LowerString({'A': 1, 'B': 2, 'C': 3}))

# TEST_3:
print("\nтест 3")
s = LowerString('BeeGeek')

print(s[0], s[3])

# TEST_4:
print("\nтест 4")
words = ['NEXT', 'SITE', 'BREAK', 'CONDITION', 'SONG', 'FEDERAL', 'CHANCE', 'LEARN', 'LARGE', 'GOAL', 'GENERAL',
         'WORKER', 'BASE', 'GROWTH', 'CARRY', 'REMEMBER', 'MODEL', 'CURRENT', 'SCIENCE', 'TEACH', 'WORD', 'WEST',
         'YEAH', 'WHERE', 'NONE', 'RELATE', 'BAR', 'AUTHOR', 'GIVE', 'SKIN', 'THOUGH', 'DECIDE', 'BOOK', 'GET', 'CLOSE',
         'ARTICLE', 'QUICKLY', 'POSITIVE', 'BODY', 'CONTROL', 'PRICE', 'CONTROL', 'SIGN', 'BED', 'CITY', 'LEAVE',
         'DECISION', 'BEAT', 'WITHIN', 'TAKE', 'MISSION', 'PRESSURE', 'IF', 'TAX', 'DREAM', 'DISCOVER', 'MAJORITY',
         'MORE', 'SKILL', 'DOG', 'NEW', 'FISH', 'EDGE', 'RECOGNIZE', 'CHILD', 'ACCORDING', 'PRACTICE', 'FINANCIAL',
         'AFTER', 'FORGET', 'SHARE', 'CONCERN', 'TRIAL', 'CONDITION', 'US', 'DEFENSE', 'SECTION', 'INSTITUTION',
         'WORKER', 'THAN', 'WRITE', 'BECAUSE', 'NATIONAL', 'MANAGER', 'CULTURAL', 'THUS', 'PERSONAL', 'SEASON', 'CAR',
         'DAY', 'EAT', 'SPEECH', 'COLLEGE', 'SMALL', 'TURN', 'CUSTOMER', 'SIMILAR', 'PUBLIC', 'OFFICER', 'FISH']

for word in words:
    print(LowerString(word))

# TEST_5:
print("\nтест 5")
print(LowerString())

# TEST_6:
print("\nтест 6")
lowerstring = LowerString()
print(type(lowerstring))
