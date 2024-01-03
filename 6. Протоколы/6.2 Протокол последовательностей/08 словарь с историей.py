"""
Реализуйте класс HistoryDict, описывающий словарь, который запоминает предыдущие значения по каждому ключу.
    При создании экземпляра класс должен принимать один аргумент:

        data — словарь, определяющий начальный набор элементов экземпляра класса HistoryDict. Если не передан,
                начальный набор элементов считается пустым

Класс HistoryDict должен иметь пять методов экземпляра:

    keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса HistoryDict
    values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра
                класса HistoryDict
    items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра
               класса HistoryDict в виде кортежей (<ключ>, <значение>)
    history() — метод, принимающий в качестве аргумента ключ и возвращающий список, элементами которого являются
                 все значения, которые когда-либо содержались в экземпляре класса HistoryDict по указанному ключу.
                 Если данный ключ не содержится в экземпляре класса HistoryDict (был удален или никогда
                 не добавлялся), метод должен вернуть пустой список
    all_history() — метод, возвращающий словарь, ключами в котором являются ключи экземпляра класса HistoryDict,
                     а значениями — списки, содержащие все значения, которые когда-либо содержались по этим ключам

При передаче экземпляра класса HistoryDict в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса HistoryDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи,
    например, с помощью цикла for.

Наконец, экземпляр класса HistoryDict должен позволять получать и изменять значения своих элементов по их ключам,
    добавлять новые пары (ключ, значение) и удалять уже имеющиеся.

Примечание 1. Экземпляр класса HistoryDict не должен зависеть от словаря, на основе которого он был создан.
              Другими словами, если исходный словарь изменится, то экземпляр класса HistoryDict измениться  не должен.

Примечание 2. Реализация класса HistoryDict может быть произвольной, то есть требований к наличию определенных
              атрибутов нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется.
              Гарантируется, что реализованный класс используется только с корректными данными.
"""


class HistoryDict:
    def __init__(self, data=()):
        self.data = dict(data) or {}
        self.history_dictionary = {k: [v, ] for k, v in self.data.items()}

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def history(self, key):
        return self.history_dictionary.get(key, [])

    def all_history(self):
        return self.history_dictionary

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.history_dictionary.setdefault(key, []).append(value)
        self.data[key] = value

    def __delitem__(self, key):
        del self.history_dictionary[key]
        del self.data[key]


# INPUT DATA:

# TEST_1:
print('\nтест 1')
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict['ducks'])
print(historydict['cats'])
print(len(historydict))

# TEST_2:
print('\nтест 2')
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(*historydict)
print(*historydict.keys())
print(*historydict.values())
print(*historydict.items())

# TEST_3:
print('\nтест 3')
historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['ducks'] = 100
print(historydict.history('ducks'))
print(historydict.history('cats'))
print(historydict.history('dogs'))

# TEST_4:
print('\nтест 4')
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict.all_history())
historydict['ducks'] = 100
historydict['ducks'] = 101
historydict['cats'] = 2
print(historydict.all_history())

# TEST_5:
print('\nтест 5')
historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['dogs'] = 1
print(len(historydict))
del historydict['ducks']
del historydict['cats']
print(len(historydict))

# TEST_6:
print('\nтест 6')
d = {'name': 'Иннокентий Елисеевич Архипов', 'age': 34, 'year': 1989}
historydict = HistoryDict(d)

names = ['Регина Ефимовна Костина', 'Мина Викторович Лаврентьев', 'Голубева Юлия Робертовна',
         'Чернова Варвара Максимовна', 'Юдин Матвей Иосипович', 'Степанов Мечислав Ерофеевич',
         'Абрамов Амос Августович', 'Ольга Егоровна Константинова', 'Хохлов Ираклий Ефимьевич',
         'Нестеров Никон Ермилович', 'Третьякова София Юльевна', 'Кудряшова Нина Юльевна', 'Казакова Раиса Феликсовна',
         'Александрова Надежда Николаевна', 'Никон Давыдович Васильев', 'Пахом Ильясович Морозов',
         'Дмитрий Тихонович Панов', 'Лебедева Галина Валериевна', 'Кузьмина Анастасия Викторовна',
         'Севастьян Жанович Якушев']

ages = [37, 20, 31, 21, 38, 24, 31, 24, 37, 20, 22, 39, 25, 21, 28, 28, 30, 30, 36, 23]

years = [1986, 2003, 1992, 2002, 1985, 1999, 1992, 1999, 1986, 2003, 2001, 1984, 1998, 2002, 1995, 1995, 1993, 1993,
         1987, 2000]

for name, age, year in zip(names, ages, years):
    historydict['name'] = name
    historydict['age'] = age
    historydict['year'] = year

print(*historydict.items())
print(historydict.history('name'))
print(historydict.history('age'))
print(historydict.history('year'))

# TEST_7:
print('\nтест 7')
historydict = HistoryDict()
print('Keys:', *historydict.keys())
print('Values:', *historydict.values())
print('Items:', *historydict.items())
print('History(key=1):', historydict.history(1))
print('History(key=1):', historydict.history(1))
print('All history:', historydict.all_history())

# TEST_8:
print('\nтест 8')
historydict = HistoryDict({'name': 'Irenica', 'country': 'Russia', 'level': 'junior', })

print(historydict.all_history())

historydict['country'] = 'Italy'
historydict['level'] = 'middle'
historydict['level'] = 'senior'

print(historydict.all_history())

del historydict['level']

print(historydict.all_history())

historydict['level'] = 'God'

print(historydict.all_history())

# TEST_9:
print('\nтест 9')
d = dict.fromkeys(range(100), None)
attrdict = HistoryDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)
