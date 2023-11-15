"""
Реализуйте класс BankAccount, описывающий банковский счет.
При создании экземпляра класс должен принимать один аргумент:

    balance — баланс счета, по умолчанию имеет значение 0

Экземпляр класса BankAccount должен иметь один атрибут:

    _balance — баланс счета

Класс BankAccount должен иметь четыре метода экземпляра:

    get_balance() — метод, возвращающий актуальный баланс счета
    deposit() — метод, принимающий в качестве аргумента число amount и увеличивающий баланс счета на amount
    withdraw() — метод, принимающий в качестве аргумента число amount и уменьшающий баланс счета на amount.
    Если amount превышает количество средств на балансе счета, должно быть возбуждено исключение
    ValueError с сообщением:

    На счете недостаточно средств

    transfer() — метод, принимающий в качестве аргументов банковский счет account и число amount.
    Метод должен уменьшать баланс текущего счета на amount и увеличивать баланс счета account на amount.
    Если amount превышает количество средств на балансе текущего счета, должно быть возбуждено исключение
    ValueError с сообщением:

    На счете недостаточно средств

Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self.get_balance() - amount >= 0:
            self._balance -= amount
        else:
            raise ValueError('На счете недостаточно средств')

    def transfer(self, account_, amount):
        self.withdraw(amount)
        account_.deposit(amount)


# INPUT DATA:

# TEST_1:
print('\nTEST 1:')
account = BankAccount()

print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())

# TEST_2:
print('\nTEST 2:')
account = BankAccount(100)

try:
    account.withdraw(150)
except ValueError as e:
    print(e)

# TEST_3:
print('\nTEST 3:')
account1 = BankAccount(100)
account2 = BankAccount(200)

account1.transfer(account2, 50)
print(account1.get_balance())
print(account2.get_balance())

# TEST_4:
print('\nTEST 4:')
account1 = BankAccount(100)
account2 = BankAccount(200)

try:
    account1.transfer(account2, 150)
except ValueError as e:
    print(e)

# TEST_5:
print('\nTEST 5:')
account1 = BankAccount(balance=100)
account2 = BankAccount(balance=0)
account1.transfer(account2, 20)
print(account1.get_balance())
print(account2.get_balance())

# TEST_6:
print('\nTEST 6:')
account = BankAccount()
print(hasattr(account, '_balance'))

# TEST_7:
print('\nTEST 7:')
account = BankAccount(balance=10)
account.withdraw(10)
print(account.get_balance())

# TEST_8:
print('\nTEST 8:')
account1 = BankAccount(balance=100)
account2 = BankAccount()
account1.transfer(account2, 100)
print(account1.get_balance())
print(account2.get_balance())
