"""
Реализуйте класс Greeter. При создании экземпляра класс должен принимать один аргумент:

    name — имя пользователя

Экземпляр класса Greeter должен иметь один атрибут:

    name — имя пользователя

Экземпляр класса Greeter должен являться контекстным менеджером, который приветствует пользователя с именем name
    перед выполнением блока with и выводит текст:

    Приветствую, <имя пользователя>!

а также прощается с ним после выполнения блока with и выводит текст:

    До встречи, <имя пользователя>!

Примечание 1. Наглядные примеры использования класса Greeter продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
                используется только с корректными данными.

Примечание 3. Класс Greeter должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__()
                и __exit__(). Реализация же протокола может быть произвольной.
"""


class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Приветствую, {self.name}!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"До встречи, {self.name}!")


# INPUT DATA:

# TEST_1:
print('\nтест 1')
with Greeter('Кейв'):
    print('...')

# TEST_2:
print('\nтест 2')
with Greeter('Кейв') as greeter:
    print(greeter.name)

# TEST_3:
print('\nтест 3')
with Greeter('Матильда') as greeter:
    pass

# TEST_4:
print('\nтест 4')
with Greeter('Михаил Г.') as greeter:
    print(
        '\nКак бессонница в час ночной\n'
        'Меняет, нелюдимая, облик твой,\n'
        'Чьих невольница ты идей?\n'
        'Зачем тебе охотиться на людей?\n'
    )

# TEST_5:
print('\nтест 5')
with Greeter('Gvido') as greeter:
    try:
        print(greeter.age)
    except AttributeError as e:
        print(f'Атрибут "{e.name}" отсутствует')
