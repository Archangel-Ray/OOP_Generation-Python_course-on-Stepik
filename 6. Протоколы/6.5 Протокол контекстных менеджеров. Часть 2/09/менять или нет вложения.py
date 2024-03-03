"""
Реализуйте класс Atomic. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

    data — произвольный список, множество или словарь
    deep — булево значение, по умолчанию равняется False

Экземпляр класса Atomic должен являться контекстным менеджером, который позволяет выполнять операции над
    коллекцией data внутри блока with в атомарном режиме, то есть либо все операции должны быть выполнены,
    либо ни одна из них. Если все операции корректны (не приводят к возбуждению исключения), они должны
    быть применены к коллекции data. Если какая-либо операция некорректна, все ранее выполненные операции
    должны быть отменены, а коллекция data должна быть возвращена в исходное состояние.

Параметр deep должен определять состояние вложенных структур коллекции data после завершения блока with.
    Если он имеет значение False, контекстный менеджер должен возвращать в исходное состояние только саму
    коллекцию data, не затрагивая ее вложенные структуры. Например, если data является двумерным списком
    и внутри блока with произошло изменение одного из его вложенных списков, то этот вложенный список
    должен сохранить свое новое состояние, даже если последующие операции внутри блока with приведут
    к возбуждению исключения и возврату коллекции data в исходное состояние. Если же параметр deep имеет
    значение True, контекстный менеджер должен возвращать в исходное состояние не только саму
    коллекцию data, но и ее вложенные структуры.

Примечание 1. Наглядные примеры использования класса Atomic продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс Atomic должен удовлетворять протоколу контекстного менеджера,
                то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.
"""
import copy


class Atomic:
    def __init__(self, data_, deep=False):
        self.data = data_
        self.temp = copy.deepcopy(self.data) if deep else self.data.copy()

    def __enter__(self):
        return self.temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_val:
            if isinstance(self.data, list):
                self.data[:] = self.temp
            else:
                self.data.clear()
                self.data.update(self.temp)
        return True


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[1]

print(numbers)

# TEST_2:
print('\nтест 2')
numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[100]  # обращение по несуществующему индексу

print(numbers)

# TEST_3:
print('\nтест 3')
matrix = [[1, 2], [3, 4]]

with Atomic(matrix) as atomic:
    atomic[1].append(0)  # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]  # обращение по несуществующему индексу

print(matrix)

# TEST_4:
print('\nтест 4')
matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)  # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]  # обращение по несуществующему индексу

print(matrix)

# TEST_5:
print('\nтест 5')
numbers = {1, 2, 3, 4, 5}

with Atomic(numbers) as atomic:
    atomic.add(6)
    atomic.append(7)  # добавление элемента с помощью несуществующего метода

print(sorted(numbers))

with Atomic(numbers) as atomic:
    atomic.add(6)

print(sorted(numbers))

# TEST_6:
print('\nтест 6')
data = {'firstname': 'Alyson', 'lastname': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

with Atomic(data, True) as atomic:  # deep = True
    atomic['birthday']['month'] = 'April'  # изменение вложенной структуры
    print(atomic['name'])  # обращение по несуществующему ключу

print(data)

with Atomic(data) as atomic:  # deep = False
    atomic['birthday']['month'] = 'April'  # изменение вложенной структуры
    print(atomic['name'])  # обращение по несуществующему ключу

print(data)

# TEST_7:
print('\nтест 7')
data = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}

with Atomic(data) as atomic:
    atomic['e'] += 2  # изменение структуры

print(data)

# TEST_8:
print('\nтест 8')
matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)

print(matrix)
