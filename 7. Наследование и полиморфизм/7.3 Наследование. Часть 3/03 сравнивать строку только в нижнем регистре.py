"""
Реализуйте класс FuzzyString, наследника класса str, описывающий строку, которая при любых
    сравнениях (==, !=, >, <, >=, <=) и проверках на принадлежность (in, not in) не учитывает регистр.
    Процесс создания экземпляра класса FuzzyString должен совпадать с процессом создания экземпляра класса str.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию,
                должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса FuzzyString нет, она может быть произвольной.
"""


class FuzzyString(str):
    def __eq__(self, other):  # ==
        if isinstance(other, str):
            return self.lower() == other.lower()
        return NotImplemented

    def __ne__(self, other):  # !=
        if isinstance(other, str):
            return self.lower() != other.lower()
        return NotImplemented

    def __lt__(self, other):  # <
        if isinstance(other, str):
            return self.lower() < other.lower()
        return NotImplemented

    def __gt__(self, other):  # >
        if isinstance(other, str):
            return self.lower() > other.lower()
        return NotImplemented

    def __le__(self, other):  # <=
        if isinstance(other, str):
            return self.lower() <= other.lower()
        return NotImplemented

    def __ge__(self, other):  # >=
        if isinstance(other, str):
            return self.lower() >= other.lower()
        return NotImplemented

    def __contains__(self, other):  # other in self
        if isinstance(other, str):
            return other.lower() in self.lower()
        return NotImplemented


# INPUT DATA:

# TEST_1:
print("\nтест 1")
s1 = FuzzyString('BeeGeek')
s2 = FuzzyString('beegeek')

print(s1 == s2)
print(s1 in s2)
print(s2 in s1)
print(s2 not in s1)

# TEST_2:
print("\nтест 2")
s = FuzzyString('BeeGeek')

print(s != 'BEEGEEK')
print(s == 'BEEGEEK')
print(s != 'beegeek')
print(s == 'beegeek')
print(s >= 'BEEGEEK')
print(s <= 'BEEGEEK')
print(s > 'BEEGEEK')
print(s < 'BEEGEEK')

# TEST_3:
print("\nтест 3")
s = FuzzyString('BeeGeek')

print(s != 'BEE GEEK')
print(s == 'BEE GEEK')
print(s != 'bee geek')
print(s == 'bee geek')

# TEST_4:
print("\nтест 4")
s = FuzzyString('patrick')

words = ['patrick', 'Patrick', 'pAtrick', 'PAtrick', 'paTrick', 'PaTrick', 'pATrick', 'PATrick', 'patRick', 'PatRick',
         'pAtRick', 'PAtRick', 'paTRick', 'PaTRick', 'pATRick', 'PATRick', 'patrIck', 'PatrIck', 'pAtrIck', 'PAtrIck',
         'paTrIck', 'PaTrIck', 'pATrIck', 'PATrIck', 'patRIck', 'PatRIck', 'pAtRIck', 'PAtRIck', 'paTRIck', 'PaTRIck',
         'pATRIck', 'PATRIck', 'patriCk', 'PatriCk', 'pAtriCk', 'PAtriCk', 'paTriCk', 'PaTriCk', 'pATriCk', 'PATriCk',
         'patRiCk', 'PatRiCk', 'pAtRiCk', 'PAtRiCk', 'paTRiCk', 'PaTRiCk', 'pATRiCk', 'PATRiCk', 'patrICk', 'PatrICk',
         'pAtrICk', 'PAtrICk', 'paTrICk', 'PaTrICk', 'pATrICk', 'PATrICk', 'patRICk', 'PatRICk', 'pAtRICk', 'PAtRICk',
         'paTRICk', 'PaTRICk', 'pATRICk', 'PATRICk', 'patricK', 'PatricK', 'pAtricK', 'PAtricK', 'paTricK', 'PaTricK',
         'pATricK', 'PATricK', 'patRicK', 'PatRicK', 'pAtRicK', 'PAtRicK', 'paTRicK', 'PaTRicK', 'pATRicK', 'PATRicK',
         'patrIcK', 'PatrIcK', 'pAtrIcK', 'PAtrIcK', 'paTrIcK', 'PaTrIcK', 'pATrIcK', 'PATrIcK', 'patRIcK', 'PatRIcK',
         'pAtRIcK', 'PAtRIcK', 'paTRIcK', 'PaTRIcK', 'pATRIcK', 'PATRIcK', 'patriCK', 'PatriCK', 'pAtriCK', 'PAtriCK',
         'paTriCK', 'PaTriCK', 'pATriCK', 'PATriCK', 'patRiCK', 'PatRiCK', 'pAtRiCK', 'PAtRiCK', 'paTRiCK', 'PaTRiCK',
         'pATRiCK', 'PATRiCK', 'patrICK', 'PatrICK', 'pAtrICK', 'PAtrICK', 'paTrICK', 'PaTrICK', 'pATrICK', 'PATrICK',
         'patRICK', 'PatRICK', 'pAtRICK', 'PAtRICK', 'paTRICK', 'PaTRICK', 'pATRICK', 'PATRICK']

print(all(s == item for item in words))

# TEST_5:
print("\nтест 5")
s1 = FuzzyString('ManTrida')
s2 = FuzzyString('MANTRIDA')

print(s1 == s2)
print(s1 != s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1 > s2)
print(s1 < s2)

# TEST_6:
print("\nтест 6")
s = FuzzyString('BeeGeek')

print(s.__eq__(1))
print(s.__ne__(1.1))
print(s.__gt__(range(5)))
print(s.__lt__([1, 2, 3]))
print(s.__ge__({4, 5, 6}))
print(s.__le__({1: 'one'}))

# TEST_7:
print("\nтест 7")
s1 = FuzzyString('BeeGeek')
s2 = FuzzyString('bee')

print(s2 in s1)
print(s1 in s2)
