"""
Требовалось реализовать класс Item, описывающий предмет. При создании экземпляра класс должен был принимать
    три аргумента в следующем порядке:

    name — название предмета
    price — цена предмета в рублях
    quantity — количество предметов

Предполагалось, что при обращении к атрибуту name экземпляра класса Item будет возвращаться его название
    с заглавной буквы, а при обращении к атрибуту total — произведение цены предмета на его количество.

Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Item.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
    Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Item нет, она может быть произвольной.
"""


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, item_):
        if item_ == 'name':
            return object.__getattribute__(self, item_).title()
        return object.__getattribute__(self, item_)

    def __getattr__(self, name):
        if name == 'total':
            return self.price * self.quantity
        raise AttributeError


# INPUT DATA:

# TEST_1:
print("\nтест 1")
fruit = Item('banana', 15, 5)

print(fruit.price)
print(fruit.quantity)

# TEST_2:
print("\nтест 2")
fruit = Item('banana', 15, 5)

print(fruit.name)
print(fruit.total)

# TEST_3:
print("\nтест 3")
course = Item('pygen', 3900, 2)

print(course.name)
print(course.price)
print(course.quantity)
print(course.total)

# TEST_4:
print("\nтест 4")
items = [
    Item('Обручальное Кольцо', 49000, 7),
    Item('Мобильный Телефон', 110000, 200),
    Item('Ноутбук', 150000, 2000),
    Item('Ручка Паркер', 37000, 20),
    Item('Статуэтка Оскар', 28000, 4000),
    Item('Наушники', 11000, 150),
    Item('Гитара', 32000, 1500),
    Item('Золотая Монета', 140000, 8),
    Item('Фотоаппарат', 79000, 720),
    Item('Лимитированные Кроссовки', 80000, 300)
]

for item in items:
    print(item.name, item.total)

# TEST_5:
print("\nтест 5")
goods = [
    Item('Морковь', 257, 20),
    Item('Лук', 251, 10),
    Item('Свекла', 120, 11),
    Item('Капуста', 280, 2),
    Item('Огурцы', 87, 5),
    Item('Помидоры', 123, 3),
    Item('Болгарский', 192, 2),
    Item('Перец', 197, 9),
    Item('Яблоки', 261, 3),
    Item('Груши', 103, 15),
    Item('Лимон', 166, 7),
    Item('Апельсины', 213, 2),
    Item('Бананы', 71, 13),
    Item('Виноград', 247, 10),
    Item('Киви', 226, 20)
]

for product in goods:
    print(product.name, product.total, 'руб.')
