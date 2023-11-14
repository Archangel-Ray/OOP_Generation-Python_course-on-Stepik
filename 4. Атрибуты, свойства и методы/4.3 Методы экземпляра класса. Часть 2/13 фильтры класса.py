"""
Реализуйте класс Postman, описывающий почтальона. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса Postman должен иметь один атрибут:

    delivery_data — изначально пустой список адресов, по которым следует доставить письма

Экземпляр класса Postman должен иметь три метода экземпляра:

    add_delivery() — метод, принимающий в качестве аргументов улицу, дом и квартиру, и добавляющий в
                      список адресов эти данные в виде кортежа:

    (<улица>, <дом>, <квартира>)

    get_houses_for_street() — метод, принимающий в качестве аргумента улицу и возвращающий список всех домов на этой
                               улице, в которые требуется доставить письма
    get_flats_for_house() — метод, принимающий в качестве аргументов улицу и дом и возвращающий список
                             всех квартир в этом доме, в которые требуется доставить письма

Примечание 1. Дома и квартиры в списках, возвращаемых методами get_houses_for_street() и get_flats_for_house(), должны
располагаться в том порядке, в котором они были добавлены.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
"""


class Postman:
    def __init__(self):
        self.delivery_data = list()

    def add_delivery(self, street, house, apartment):
        self.delivery_data.append((street, house, apartment))

    def get_houses_for_street(self, street):
        list_house = []
        for address in self.delivery_data:
            if address[0] == street:
                if address[1] not in list_house:
                    list_house.append(address[1])
        return list_house

    def get_flats_for_house(self, street, house):
        list_apartment = []
        for address in self.delivery_data:
            if address[0] == street and address[1] == house:
                if address[2] not in list_apartment:
                    list_apartment.append(address[2])
        return list_apartment


# INPUT DATA:

# TEST_1:
postman = Postman()

print(postman.delivery_data)
print(postman.get_houses_for_street('3-я ул. Строителей'))
print(postman.get_flats_for_house('3-я ул. Строителей', 25))

# TEST_2:
postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))

# TEST_3:
postman = Postman()

delivery_data = [('Тульская', 149, 35), ('Запорожская', 19, 26), ('Сосновая', 33, 17), ('Высотная', 91, 44),
                 ('Шишкина', 143, 8), ('Иванова', 60, 38), ('Веселая', 115, 19), ('Учительская', 37, 70),
                 ('М.Горького', 167, 57), ('Северная', 128, 44), ('Железнодорожная', 121, 28), ('Пригородная', 39, 2),
                 ('Одесская', 176, 34), ('Высоцкого', 100, 24), ('Цветочная', 168, 49), ('Павлова', 35, 62),
                 ('Шолохова', 177, 8), ('Баумана', 27, 96), ('Димитрова', 170, 37), ('Папанина', 85, 59),
                 ('40 лет Победы', 167, 56), ('Весенняя', 165, 63), ('Дарвина', 77, 39), ('Лунная', 200, 79),
                 ('Иванова', 104, 20), ('Комсомольская', 38, 74), ('Дарвина', 149, 44), ('Льва Толстого', 174, 85),
                 ('Победы', 64, 45), ('Новоселов', 128, 22)]

for delivery in delivery_data:
    postman.add_delivery(*delivery)

print(postman.get_houses_for_street('Дарвина'))
print(postman.get_flats_for_house('Новоселов', 128))
