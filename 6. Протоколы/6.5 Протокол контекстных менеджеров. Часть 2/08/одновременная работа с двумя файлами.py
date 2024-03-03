"""
Реализуйте класс WriteSpy. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

    file1 — файловый объект
    file2 — файловый объект
    to_close — булево значение, по умолчанию равняется False

Экземпляр класса WriteSpy должен являться контекстным менеджером, который выполняет операцию записи сразу в оба
    файловых объекта file1 и file2. Параметр to_close должен определять состояние файловых объектов file1 и file2
    после завершения блока with. Если он имеет значение True, после завершения блока with контекстный менеджер
    должен закрыть оба файловых объекта, если False — оставить открытыми.

Класс WriteSpy должен иметь четыре метода экземпляра:

    write() — метод, принимающий в качестве аргумента текст и записывающий его в оба файловых объекта.
                Если хотя бы один из файловых объектов закрыт или недоступен для записи, должно быть
                возбуждено исключение ValueError с текстом:

                Файл закрыт или недоступен для записи

    close() — метод, немедленно закрывающий оба файловых объекта
    writable() — метод, возвращающий True, если оба файловых объекта доступны для записи, или False в противном случае
    closed() — метод, возвращающий True, если оба файловых объекта закрыты, или False в противном случае

Примечание 1. Наглядные примеры использования класса WriteSpy продемонстрированы в тестовых данных.

Примечание 2. Для проверки того, является ли файловый объект доступным для записи, используйте метод writable().
                Данный метод возвращает True, если файловый объект доступен для записи, или False в противном случае.
                При попытке применить метод на закрытом файловом объекте будет возбуждено исключение.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
                используется только с корректными данными.
основная проблема это понять условие. по сути я методом тыка подтосовывал результат.

Примечание 4. Класс WriteSpy должен удовлетворять протоколу контекстного менеджера, то есть иметь
                методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.
"""


class WriteSpy:
    def __init__(self, file1_, file2_, to_close=False):
        self.file1 = file1_
        self.file2 = file2_
        self.to_close = to_close

    def write(self, text):
        if self.writable():
            self.file1.write(text)
            self.file2.write(text)
        else:
            raise ValueError("Файл закрыт или недоступен для записи")

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        if not self.file1.closed and not self.file2.closed:
            return True if self.file1.writable() and self.file2.writable()else False
        else:
            return False

    def closed(self):
        return True if self.file1.closed and self.file2.closed else False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.close()


# INPUT DATA:

# TEST_1:
print('\nтест 1')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    combined.write('You shall seal the blinding light that plagues their dreams\n')
    combined.write('You are the Vessel\n')
    combined.write('You are the Hollow Knight')

print(f1.closed, f2.closed)

with open('file1.txt') as file1, open('file2.txt') as file2:
    print(file1.read())
    print(file2.read())


# TEST_2:
print('\nтест 2')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())

f1 = open('file1.txt')
f2 = open('file2.txt')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())

# TEST_3:
print('\nтест 3')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.closed())
    f1.close()
    print(combined.closed())
    f2.close()
    print(combined.closed())

# TEST_4:
print('\nтест 4')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=False) as combined:
    print(f1.closed, f2.closed)
    combined.close()
    print(f1.closed, f2.closed)

# TEST_5:
print('\nтест 5')
f1 = open('file1.txt', mode='r')
f2 = open('file2.txt', mode='w')

try:
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('No cost too great')
except ValueError as error:
    print(error)

# TEST_6:
print('\nтест 6')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
f1.close()

try:
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('No cost too great')
except ValueError as error:
    print(error)

# TEST_7:
print('\nтест 7')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
f1.close()

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())

# TEST_8:
print('\nтест 8')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    pass

print(combined.closed())

# TEST_9:
print('\nтест 9')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2) as combined:
    pass

print(combined.closed())
