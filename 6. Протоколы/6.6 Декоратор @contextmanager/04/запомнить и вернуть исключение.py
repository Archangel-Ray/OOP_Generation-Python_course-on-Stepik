"""
Реализуйте контекстный менеджер safe_open с помощью декоратора @contextmanager,
    который принимает два аргумента в следующем порядке:

    filename — имя файла
    mode — режим открытия файла (r, w, a и так далее), по умолчанию имеет значение r

Контекстный менеджер должен открывать файл с именем filename в режиме mode и позволять выполнять с ним
    соответствующие операции. Причем если открытие файла было выполнено без исключений, в качестве значения,
    используемого в блоке with, контекстный менеджер должен вернуть кортеж из двух элементов, первым из
    которых является необходимый файловый объект, вторым — значение None. Однако если при открытии файла
    было возбуждено исключение, то в качестве значения, используемого в блоке with, контекстный менеджер
    должен вернуть кортеж из двух элементов, первым из которых является значение None, вторым — возбужденное
    при открытии исключение. Также контекстный менеджер должен закрывать открытый им файл после выполнения
    кода внутри блока with.

Примечание 1. Наглядные примеры использования контекстного менеджера safe_open продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.
"""
from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode="r"):
    open_file = None
    try:
        open_file = open(filename, mode=mode)
        yield open_file, None
    except Exception as err:
        yield None, err
    finally:
        if open_file:
            open_file.close()


# INPUT DATA:

# TEST_1:
print("\nтест 1")
with open('Ellies_jokes.txt', 'w') as file:
    file.write('Знаешь, кто не прав? Лев\n')
    file.write('Что треугольник сказал кругу? Катись отсюда')

with safe_open('Ellies_jokes.txt') as file:
    file, error = file
    print(error)
    print(file.read())

# TEST_2:
print("\nтест 2")
with safe_open('Ellies_jokes_2.txt') as file:
    file, error = file
    print(file)
    print(error)

# TEST_3:
print("\nтест 3")
text = '''Кричит ворона в небе: – Кар-р!
В лесу пожар-р, в лесу пожар-р!
А было просто очень:
В нём поселилась осень.'''

with open('file.txt', 'w', encoding='utf-8') as file:
    file.write(text)

with safe_open('file.txt', 'r') as file:
    file, error = file
    print(file.read())
    print(error)

# TEST_4:
print("\nтест 4")
with open('file.txt', 'w') as file:
    file.write('Как говорится, земля круглая, за углом встретимся.')

with safe_open('file.txt', 'rb') as file:
    f, error = file
    print(f)
    print(error)

# TEST_5:
print("\nтест 5")
files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt', 'file6.txt', 'file7.txt', 'file8.txt',
         'file9.txt', 'file10.txt', 'file11.txt', 'file12.txt', 'file13.txt', 'file14.txt', 'file15.txt', 'file16.txt',
         'file17.txt', 'file18.txt', 'file19.txt', 'file20.txt']

for f in files:
    with safe_open(f) as file:
        file, error = file
        print(file)
        print(error)

# TEST_6:
print("\nтест 6")
with open('Couplet.txt', 'w') as file:
    file.write('Так уносились мы мечтой\n')
    file.write('К началу жизни молодой')

with safe_open('Couplet.txt') as file:
    file, error = file
    print(error)
    print(file.read())

    print(file.closed)

print(file.closed)
