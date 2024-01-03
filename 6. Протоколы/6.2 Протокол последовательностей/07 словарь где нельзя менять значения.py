"""
Реализуйте класс PermaDict, описывающий словарь, который позволяет добавлять и удалять пары (<ключ>, <значение>), но не
    позволяет изменять значения по уже имеющимся ключам. При создании экземпляра класс должен принимать один аргумент:

        data — словарь, определяющий начальный набор элементов экземпляра класса PermaDict.
                Если не передан, начальный набор элементов считается пустым

Класс PermaDict должен иметь три метода экземпляра:

    keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса PermaDict
    values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей
                экземпляра класса PermaDict
    items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса PermaDict
                в виде кортежей (<ключ>, <значение>)

При передаче экземпляра класса PermaDict в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса PermaDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например,
    с помощью цикла for.

Наконец, экземпляр класса PermaDict должен позволять получать значения своих элементов по их ключам,
    добавлять новые пары (ключ, значение) и удалять уже имеющиеся с помощью оператора del.
    При этом изменение значений по уже имеющимся ключам должно быть недоступно, и при попытке
    выполнения такой операции должно возбуждаться исключение KeyError с текстом:

    Изменение значения по ключу невозможно

Примечание 1. Экземпляр класса PermaDict не должен зависеть от словаря, на основе которого он был создан.
                Другими словами, если исходный словарь изменится, то экземпляр класса PermaDict измениться  не должен.

Примечание 2. Реализация класса PermaDict может быть произвольной,
                то есть требований к наличию определенных атрибутов нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.
"""


class PermaDict:
    def __init__(self, data=()):
        self.data = dict(data) or {}

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, item):
        return self.data.get(item)

    def __setitem__(self, key, value):
        if key not in self.data:
            self.data[key] = value
        else:
            raise KeyError('Изменение значения по ключу невозможно')

    def __delitem__(self, key):
        del self.data[key]


# INPUT DATA:

# TEST_1:
print('\nтест 1')
permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

print(permadict['name'])
print(len(permadict))

# TEST_2:
print('\nтест 2')
permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})

print(*permadict)
print(*permadict.keys())
print(*permadict.values())
print(*permadict.items())

# TEST_3:
print('\nтест 3')
permadict = PermaDict()

permadict['name'] = 'Timur'
permadict['age'] = 30
del permadict['name']
print(permadict['age'])
print(len(permadict))

# TEST_4:
print('\nтест 4')
permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

try:
    permadict['name'] = 'Arthur'
except KeyError as e:
    print(e)

# TEST_5:
print('\nтест 5')
d = dict.fromkeys(range(100), None)
attrdict = PermaDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)

# TEST_6:
print('\nтест 6')
d = {'Ерофей Всеволодович Сидоров': '13.05.1985', 'Семенов Андрон Денисович': '24.03.1988',
     'Петухова Лукия Максимовна': '15.06.1993', 'Лидия Георгиевна Фадеева': '25.12.1980',
     'Федотова Надежда Юрьевна': '04.06.1992', 'Харитонов Варфоломей Марсович': '14.06.1994',
     'Глафира Феликсовна Фомина': '29.08.1984', 'Пелагея Николаевна Брагина': '01.04.1986',
     'Никита Ильясович Макаров': '29.08.1992', 'Лихачева Майя Алексеевна': '12.11.1991',
     'Виноградова Нина Олеговна': '07.08.1992', 'Артемьева Кира Валентиновна': '11.04.1997',
     'Василиса Федоровна Уварова': '03.05.1981', 'Денисов Варфоломей Устинович': '17.04.1990',
     'Тихонова Клавдия Филипповна': '18.11.1988', 'Зимина Любовь Викторовна': '23.06.1983',
     'Кудряшов Викторин Фомич': '27.06.1997', 'Юлия Вениаминовна Ефимова': '20.10.1987',
     'Никандр Валерианович Мельников': '10.02.1985', 'Устинова Лидия Артемовна': '30.06.1992'}

permadict = PermaDict(d)

for key in permadict.keys():
    print(key, end='; ')

print('\n')

for value in permadict.values():
    print(value, end='; ')

print('\n')

for item in permadict.items():
    print(item, end='; ')

# TEST_7:
print('\nтест 7')
permadict = PermaDict()
print('Keys:', *permadict.keys())
print('Values:', *permadict.values())
print('Items:', *permadict.items())
