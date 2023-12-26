"""
Реализуйте класс DevelopmentTeam, описывающий команду разработчиков двух уровней: junior (младший) и senior (старший).
При создании экземпляра класс не должен принимать никаких аргументов.

Класс DevelopmentTeam должен иметь два метода экземпляра:

    add_junior() — метод, принимающий произвольное количество позиционных аргументов,
                    каждый из которых является именем разработчика, и добавляющий их в число junior-разработчиков
    add_senior() — метод, принимающий произвольное количество позиционных аргументов,
                    каждый из которых является именем разработчика, и добавляющий их в число senior-разработчиков

Экземпляр класса DevelopmentTeam должен быть итерируемым объектом, элементами которого сперва являются все его
junior-разработчики, а затем — все senior-разработчики. Junior-разработчики должны быть представлены в виде кортежей:

(<имя разработчика>, 'junior')

в то время как senior-разработчики — в виде кортежей:

(<имя разработчика>, 'senior')

Примечание 1. Разработчики в группах должны располагаться в том порядке, в котором они были добавлены.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса DevelopmentTeam нет, она может быть произвольной.
"""


class DevelopmentTeam:
    def __init__(self):
        self.juniors = []
        self.seniors = []

    def add_junior(self, *args):
        self.juniors.extend(args)

    def add_senior(self, *args):
        self.seniors.extend(args)

    def __iter__(self):
        for name in self.juniors:
            yield (name, 'junior')
        for name in self.seniors:
            yield (name, 'senior')


# INPUT DATA:

# TEST_1:
print('\nтест 1')
beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
beegeek.add_senior('Gvido')
print(*beegeek, sep='\n')

# TEST_2:
print('\nтест 2')
beegeek = DevelopmentTeam()

print(len(list(beegeek)))

# TEST_3:
print('\nтест 3')
beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
print(*beegeek, sep='\n')

# TEST_4:
print('\nтест 4')
beegeek = DevelopmentTeam()

beegeek.add_senior('Arthur', 'Valery', 'Timur')
print(*beegeek, sep='\n')

# TEST_5:
print('\nтест 5')
smart_monkey = DevelopmentTeam()

smart_monkey.add_senior('Gvido', 'Alan')
smart_monkey.add_junior('Denis')

print(list(smart_monkey))

# TEST_6:
print('\nтест 6')
pied_piper = DevelopmentTeam()

pied_piper.add_senior('Richard', 'Gilfoyle', 'Dinesh', 'Erlich')
pied_piper.add_junior('Jared', 'Big Head')

print(*pied_piper, sep='\n')
print(len(list(pied_piper)))
