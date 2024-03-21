"""
1. Реализуйте класс Item, описывающий товар. При создании экземпляра класс должен принимать
    два аргумента в следующем порядке:

    name — название товара
    price — цена товара в долларах

Экземпляр класса Item должен иметь следующее неформальное строковое представление:

<название товара>, <цена товара>$

2. Также реализуйте класс ShoppingCart, описывающий корзину для покупок. При создании экземпляра класс должен
    принимать один аргумент:

    items — итерируемый объект, определяющий начальный набор товаров в корзине.
            Если не передан, корзина считается пустой

Класс ShoppingCart должен иметь три метода экземпляра:

    add() — метод, принимающий в качестве аргумента товар и добавляющий его в корзину
    total() — метод, возвращающий суммарную стоимость всех товаров в корзине
    remove() — метод, принимающий в качестве аргумента название товара и удаляющий его из корзины.
                Если в корзине несколько товаров с указанным именем, они должны быть удалены все

Экземпляр класса ShoppingCart должен иметь следующее неформальное строковое представление:

<название первого товара в корзине>, <цена первого товара в корзине>$
<название второго товара в корзине>, <цена второго товара в корзине>$
...

Примечание 1. Если корзина для покупок пуста, то ее неформальным строковым представлением должна быть пустая строка.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
"""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}, {self.price}$"


class ShoppingCart:
    def __init__(self, items=()):
        self.items = items if items else []

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(x.price for x in self.items)

    def remove(self, item):
        while item in [x.name for x in self.items]:
            for n in self.items:
                if item == n.name:
                    self.items.remove(n)

    def __str__(self):
        return "\n".join([x.__str__() for x in self.items])


# INPUT DATA:

print("\n# TEST_1:")
item1 = Item('Yoga Mat', 130)
item2 = Item('Flannel Shirt', 22)

print(item1)
print(item2)

print("\n# TEST_2:")
shopping_cart = ShoppingCart([Item('Yoga Mat', 130)])

shopping_cart.add(Item('Flannel Shirt', 22))
print(shopping_cart)
print(shopping_cart.total())

print("\n# TEST_3:")
shopping_cart = ShoppingCart([Item('Yoga Mat', 130), Item('Flannel Shirt', 22)])

shopping_cart.remove('Yoga Mat')
print(shopping_cart)
print(shopping_cart.total())

print("\n# TEST_4:")
shopping_cart = ShoppingCart(
    [Item('Banana', 100), Item('Apple', 120), Item('Orange', 110), Item('Tomato', 180), Item('Cucumber', 150)])

shopping_cart.add(Item('Banana', 100))
print(shopping_cart)
print(shopping_cart.total())

shopping_cart.remove('Banana')
print(shopping_cart)
print(shopping_cart.total())

print("\n# TEST_5:")
shopping_cart = ShoppingCart()
print(shopping_cart)
