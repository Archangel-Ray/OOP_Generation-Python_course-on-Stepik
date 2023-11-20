"""
Реализуйте класс Pet, описывающий домашнее животное. При создании экземпляра класс должен принимать один аргумент:

    name — имя домашнего животного

Экземпляр класса Pet должен иметь один атрибут:

    name — имя домашнего животного

Класс Pet должен иметь три метода класса:

    first_pet() — метод, возвращающий самый первый созданный экземпляр класса Pet.
                   Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
    last_pet() — метод, возвращающий самый последний созданный экземпляр класса Pet.
                  Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
    num_of_pets() — метод, возвращающий количество созданных экземпляров класса Pet

Примечание 1. Никаких ограничений касательно реализации класса Pet нет, она может быть произвольной.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Pet:
    there_is_first_pet = None
    there_is_last_pet = None
    count_pets = 0

    def __init__(self, name_):
        self.name = name_

        if self.__class__.there_is_first_pet is None:
            self.__class__.there_is_first_pet = self
        self.__class__.there_is_last_pet = self
        self.__class__.count_pets += 1

    @classmethod
    def first_pet(cls):
        return cls.there_is_first_pet

    @classmethod
    def last_pet(cls):
        return cls.there_is_last_pet

    @classmethod
    def num_of_pets(cls):
        return cls.count_pets


# INPUT DATA:

# TEST_1:
# print('\nтест 1')
# print(Pet.first_pet())
# print(Pet.last_pet())
# print(Pet.num_of_pets())

# TEST_2:
# print('\nтест 2')
# pet1 = Pet('Ratchet')
# pet2 = Pet('Clank')
# pet3 = Pet('Rivet')

# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())

# TEST_3:
print('\nтест 3')
names = ['Mia', 'Tutti', 'Erin', 'Loki', 'Kelly', 'Hussy', 'Abbey', 'Luna', 'Isha', 'Diva', 'Brandy', 'Petra',
         'Mandy', 'Baby', 'Caitlyn', 'Taffy', 'Odie', 'Roxxy', 'Gabby', 'Shelby', 'Dolly', 'Ashley', 'Vanilla', 'Cori']

for name in names:
    pet = Pet(name)

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())

# TEST_4:
# print('\nтест 4')
# pet_ = Pet('Кемаль')
#
# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())

# TEST_5:
# print('\nтест 5')
# pet1_ = Pet('Ratchet')
# pet2_ = Pet('Clank')
# pet3_ = Pet('Rivet')
# pet4_ = Pet('Ratchet')
# pet5_ = Pet('Ratchet')
#
# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())
