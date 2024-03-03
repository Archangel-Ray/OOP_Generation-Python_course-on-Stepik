"""
Реализуйте класс Reloopable. При создании экземпляра класс должен принимать один аргумент:

    file — открытый на чтение файловый объект

Экземпляр класса Reloopable должен являться контекстным менеджером, который позволяет многократно итерироваться
    по файловому объекту file внутри блока with. Также контекстный менеджер должен закрывать используемый им файловый
    объект после выполнения кода внутри блока with.

Примечание 1. Наглядные примеры использования класса Reloopable продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс Reloopable должен удовлетворять протоколу контекстного менеджера, то есть иметь
                методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.
"""


class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self.file.readlines()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# INPUT DATA:

# TEST_1:
with open('file.txt', 'w') as file:
    file.write('Evil is evil\n')
    file.write('Lesser, greater, middling\n')
    file.write('Makes no difference\n')

with Reloopable(open('file.txt')) as reloopable:
    for line in reloopable:
        print(line.strip())
    for line in reloopable:
        print(line.strip())

# TEST_2:
with open('file.txt', 'w') as file:
    pass

file = open('file.txt')
print(file.closed)

with Reloopable(file) as reloopable:
    pass

print(file.closed)

# TEST_3:
with open('file.txt', 'w') as file:
    print(
        'Есть всего два типа языков программирования: те, '
        'на которые люди всё время ругаются, '
        'и те, которые никто не использует.',
        file=file)

file = open('file.txt')

with Reloopable(file) as reloopable:
    for _ in range(20):
        for line in reloopable:
            print(line.strip())

# TEST_4:
files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt', 'file6.txt', 'file7.txt', 'file8.txt',
         'file9.txt', 'file10.txt', 'file11.txt', 'file12.txt', 'file13.txt', 'file14.txt', 'file15.txt', 'file16.txt',
         'file17.txt', 'file18.txt', 'file19.txt', 'file20.txt']

for file in files:
    with open(file, 'w') as f:
        pass

    f = open(file)
    print(f.closed)

    with Reloopable(f) as reloopable:
        pass

    print(f.closed)
