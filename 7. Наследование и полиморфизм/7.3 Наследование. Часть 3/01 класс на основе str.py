"""
Реализуйте класс UpperPrintString, наследника класса str, описывающий строку. Процесс создания экземпляра
    класса UpperPrintString должен совпадать с процессом создания экземпляра класса str.

Экземпляр класса UpperPrintString должен иметь следующее неформальное строковое представление:

<значение строки в верхнем регистре>

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса UpperPrintString нет, она может быть произвольной.
"""


class UpperPrintString(str):
    def __str__(self):
        return super().__str__().upper()


# INPUT DATA:

# TEST_1:
print("\nтест 1")
s1 = UpperPrintString('beegeek')
s2 = UpperPrintString('BeeGeek')

print(s1)
print(s2)

# TEST_2:
print("\nтест 2")
s = UpperPrintString('beegeek')
print(list(s))

# TEST_3:
print("\nтест 3")
strings = [UpperPrintString('beegeek'), UpperPrintString('BeeGeek')]
print(strings)

# TEST_4:
print("\nтест 4")
s1 = UpperPrintString('BEEgeek')
s2 = UpperPrintString('BeeGeek')

print(s1)
print(s2)
print(s1 == s2)

# TEST_5:
print("\nтест 5")
words = ['generation', 'might', 'sign', 'doctor', 'there', 'natural', 'medical', 'staff', 'interest', 'painting',
         'chance', 'nature', 'couple', 'edge', 'fine', 'when', 'knowledge', 'when', 'nor', 'economy', 'above', 'call',
         'establish', 'wait', 'hair', 'talk', 'stand', 'behind', 'pass', 'become', 'bed', 'own', 'particular', 'box',
         'government', 'especially', 'yet', 'case', 'citizen', 'five', 'mother', 'particular', 'believe', 'poor',
         'girl', 'standard', 'perhaps', 'alone', 'door', 'whose', 'sound', 'seven', 'treatment', 'indicate',
         'particularly', 'cup', 'stay', 'organization', 'should', 'after', 'billion', 'all', 'many', 'remain', 'five',
         'drive', 'crime', 'traditional', 'represent', 'into', 'across', 'increase', 'remain', 'conference', 'there',
         'person', 'send', 'bed', 'face', 'effect', 'process', 'beyond', 'civil', 'coach', 'his', 'whole', 'hit',
         'save', 'social', 'include', 'hope', 'write', 'land', 'approach', 'do', 'letter', 'anyone', 'fast', 'theory',
         'sit']

for word in words:
    print(UpperPrintString(word))

# TEST_6:
print("\nтест 6")
print(issubclass(UpperPrintString, str))
