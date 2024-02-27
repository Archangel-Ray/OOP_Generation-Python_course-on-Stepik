"""
Лог-файл — это текстовый файл, в который автоматически записывается важная информация о работе системы или программы.
    Форматов лог-файла довольно много, однако в рамках этой задачи будем считать,
    что все лог-файлы имеют следующий единый формат:

    2022-01-01 INFO: User logged in
    2022-01-01 ERROR: Invalid input data
    2022-01-01 WARNING: File not found
    2022-01-02 INFO: User logged out
    2022-01-03 INFO: User registered

То есть каждая строка лог-файла описывает некоторое событие, которое характеризуется датой в формате YYYY-MM-DD,
    типом и кратким описанием.

Реализуйте функцию log_for(), которая принимает два аргумента в следующем порядке:

    logfile — имя лог-файла
    date_str — строковая дата в формате YYYY-MM-DD

Функция должна создавать текстовый файл с именем:

log_for_<date_str>.txt

и записывать в него все события из файла logfile, которые произошли в дату date_str.
    События должны записываться без указания даты, а также располагаться в своем исходном порядке.

Примечание 1. Имя файла, передаваемого в функцию, уже содержит расширение.

Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.
"""
from re import search


def log_for(logfile, date_str):
    with open(logfile, encoding='utf-8') as reading, \
            open(f'log_for_{date_str}.txt', mode='w', encoding='utf-8') as writing:
        for row in reading.readlines():
            date, event = search(r"(\d{4}-\d{2}-\d{2}) (.*)", row).groups()
            if date == date_str:
                print(event, file=writing)


# INPUT DATA:

# TEST_1:
with open('log.txt', 'w', encoding='utf-8') as file:
    print('2022-01-01 INFO: User logged in', file=file)
    print('2022-01-01 ERROR: Invalid input data', file=file)
    print('2022-01-02 INFO: User logged out', file=file)
    print('2022-01-03 INFO: User registered', file=file)

log_for('log.txt', '2022-01-01')

with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
    print(file.read())

# TEST_2:
data = '''2022-01-07 INFO: User is here
2022-01-15 INFO: Username is True
2022-01-29 INFO: Engine started
2022-01-02 INFO: Hello world
2022-01-03 INFO: Engine started
2022-01-11 ERROR: File not found
2022-01-31 ERROR: Shaders not supported
2022-01-07 ERROR: User is nub
2022-01-11 ERROR: CPU not found
2022-01-07 INFO: Patrick
2022-01-25 INFO: Engine started
2022-01-15 INFO: I`am glad
2022-01-07 ERROR: File not found
2022-01-07 INFO: Start Beegeek OOP Course
2022-01-17 INFO: It`s amazing!
2022-01-25 ERROR: File not found
2022-01-06 INFO: Engine started
2022-01-25 INFO: Algorithms
2022-01-09 ERROR: Shaders not supported
2022-01-07 INFO: Goodbye'''

with open('log.txt', 'w', encoding='utf-8') as file:
    print(data, file=file)

log_for('log.txt', '2022-01-07')

with open('log_for_2022-01-07.txt', encoding='utf-8') as file:
    print(file.read())
