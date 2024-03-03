"""
Реализуйте контекстный менеджер safe_write с помощью декоратора @contextmanager, который принимает один аргумент:

    filename — имя файла

Контекстный менеджер должен позволять записывать информацию в файл с именем filename. Причем если во время записи
    в файл было возбуждено какое-либо исключение, контекстный менеджер должен поглотить его, отменить все выполненные
    ранее записи в файл, если они были, вернуть файл в исходное состояние и проинформировать о возбужденном исключении
    выводом следующего текста:

    Во время записи в файл было возбуждено исключение <тип исключения>

Примечание 1. Наглядные примеры использования контекстного менеджера safe_write продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.
"""
from contextlib import contextmanager


@contextmanager
def safe_write(filename):
    temp = open("temp.txt", 'w')
    file_ = None
    try:
        yield temp
        temp.close()
        file_ = open(filename, 'w')
        file_.write(open("temp.txt").read())
    except Exception as err:
        print(f"Во время записи в файл было возбуждено исключение {type(err).__name__}")
    finally:
        temp.close()
        if file_:
            file_.close()


# INPUT DATA:

# TEST_1:
print("\nтест 1")
with safe_write('undertale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью')

with open('undertale.txt') as file:
    print(file.read())

# TEST_2:
print("\nтест 2")
with safe_write('under_tale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')

with safe_write('under_tale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
    raise ValueError

with open('under_tale.txt') as file:
    print(file.read())

# TEST_3:
print("\nтест 3")
with safe_write('poem.txt') as file:
    print('''Я кашлянул в звенящей тишине,
И от шального эха стало жутко…,
Расскажет ли утятам обо мне,
под утро мной испуганная утка?''', file=file)

with safe_write('poem.txt') as file:
    file.insert('Стихотворение про утку')  # неверный метод для записи в файл

with open('poem.txt') as file:
    print(file.read())
