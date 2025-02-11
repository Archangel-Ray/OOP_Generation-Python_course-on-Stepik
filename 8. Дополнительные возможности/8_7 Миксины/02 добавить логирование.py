"""
Реализуйте класс LoggerMixin, добавляющий классам функционал логирования.

Класс LoggerMixin должен иметь один метод экземпляра:

log() — метод, принимающий в качестве аргументов уровень логирования и текст сообщения, и выводящий информацию
    о событии в следующем формате:

[<текущие дата и время>] - <уровень логирования> - <имя класса, которому добавляется функционал логирования>: <текст
    сообщения>

Текущие дата и время должны быть представлены в формате DD.MM.YYYY HH:MM:SS.

Примечание 1. Текущие дата и время, которые содержит строка логирования, выводимая методом log(), могут отличаться от
    значений, представленных в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
    используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса LoggerMixin нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/OOP/tree/main/Module_8/Module_8.7/Module_8.7.11
"""
from datetime import datetime


class LoggerMixin:
    def log(self, level, message):
        print(f"[{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}] - {level} - {self.__class__.__name__}: {message}")


# INPUT DATA:

# TEST_1:
class Database(LoggerMixin):
    def connect(self):
        self.log('INFO', 'Выполнено подключение к базе данных.')

    def disconnect(self):
        self.log('INFO', 'Подключение к базе данных закрыто.')


db = Database()
db.connect()
db.disconnect()


# TEST_2:
class Order(LoggerMixin):
    def __init__(self, order_id):
        self.order_id = order_id

    def create_order(self):
        self.log('INFO', f'Заказ № {self.order_id} создан.')

    def cancel_order(self):
        self.log('WARNING', f'Заказ № {self.order_id} отменен.')


order1 = Order(9876287)
order1.create_order()

order2 = Order(4778616)
order2.create_order()
order2.cancel_order()


# TEST_3:
class Subscription(LoggerMixin):
    def subscribe_user(self, user_id):
        self.log('INFO', f'Пользователь id={user_id} купил подписку.')

    def unsubscribe_user(self, user_id):
        self.log('WARNING', f'Пользователь id={user_id} отменил подписку.')

    def subscription_update_failed(self, user_id):
        self.log('ERROR', f'Не удалось обновить подписку пользователя id={user_id}.')


subscription = Subscription()
subscription.subscribe_user(32720521)
subscription.unsubscribe_user(90843698)
subscription.subscription_update_failed(73520485)


# TEST_4:
class Inventory(LoggerMixin):
    def check_stock(self, product_name, quantity):
        if quantity > 5:
            self.log('INFO', f'Количество товара "{product_name}" на складе = {quantity}.')
        elif 1 <= quantity <= 5:
            self.log('WARNING', f'Товар "{product_name}" заканчивается на складе. Количество товара = {quantity}.')
        elif quantity == 0:
            self.log('WARNING', f'Товар "{product_name}" отсутствует на складе.')
        else:
            self.log('ERROR', f'Не удалось проверить наличие товара "{product_name}" на складе.')


inventory = Inventory()
inventory.check_stock('Ручка', 54)
inventory.check_stock('Карандаш', 13)
inventory.check_stock('Тетрадь', 3)
inventory.check_stock('Ластик', 0)
inventory.check_stock('Линейка', -1)
