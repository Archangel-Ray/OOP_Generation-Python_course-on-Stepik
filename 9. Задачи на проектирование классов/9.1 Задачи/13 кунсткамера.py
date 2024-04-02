"""
Реализуйте класс MultiKeyDict, который практически во всем повторяет класс dict. Создание экземпляра
    класса MultiKeyDict должно происходить аналогично созданию экземпляра класса dict:

    multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
    multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])

    print(multikeydict1['x'])        # 1
    print(multikeydict2['z'])        # 3

Особенностью класса MultiKeyDict должен являться метод alias(), который должен позволять давать имеющимся ключам
    псевдонимы. Обращение по созданному псевдониму не должно ничем отличаться от обращения по оригинальному ключу,
    то есть с момента создания псевдонима у значения становится два ключа (или больше, если псевдонимов несколько):

    multikeydict = MultiKeyDict(x=100, y=[10, 20])

    multikeydict.alias('x', 'z')     # добавление ключу 'x' псевдонима 'z'
    multikeydict.alias('x', 't')     # добавление ключу 'x' псевдонима 't'
    print(multikeydict['z'])         # 100
    multikeydict['t'] += 1
    print(multikeydict['x'])         # 101

    multikeydict.alias('y', 'z')     # теперь 'z' становится псевдонимом ключа 'y'
    multikeydict['z'] += [30]
    print(multikeydict['y'])         # [10, 20, 30]

Значение должно оставаться доступным по псевдониму даже в том случае, если оригинальный ключ был удален:

    multikeydict = MultiKeyDict(x=100)

    multikeydict.alias('x', 'z')
    del multikeydict['x']
    print(multikeydict['z'])         # 100

Ключи должны иметь приоритет над псевдонимами. Если некоторые ключ и псевдоним совпадают, то все операции при
    обращении к ним должны выполняться именно с ключом:

    multikeydict = MultiKeyDict(x=100, y=[10, 20])

    multikeydict.alias('x', 'y')
    print(multikeydict['y'])         # [10, 20]
"""
from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self.dict_alias = {}
        super().__init__(*args, **kwargs)

    def alias(self, item, new_item):
        self.dict_alias[new_item] = item

    def __getitem__(self, item):
        if item not in self.data:
            return self.data[self.dict_alias[item]]
        return self.data[item]

    def __setitem__(self, key, value):
        if key not in self.data:
            if key in self.dict_alias:
                self.data[self.dict_alias[key]] = value
            else:
                self.data[key] = value
        else:
            self.data[key] = value

    def __delitem__(self, key):
        if key in self.dict_alias.values():
            new = None
            for k, v in self.dict_alias.items():
                if v == key:
                    if new is None:
                        new = k
                        self.data[k] = self.data[key]
                    else:
                        self.dict_alias[k] = new
            del self.dict_alias[new]
            del self.data[key]
        else:
            del self.data[key]


# INPUT DATA:

print("\n# TEST_1:")
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'z')
multikeydict.alias('x', 't')
print(multikeydict['z'])
multikeydict['t'] += 1
print(multikeydict['x'])

multikeydict.alias('y', 'z')
multikeydict['z'] += [30]
print(multikeydict['y'])

print("\n# TEST_2:")
multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
del multikeydict['x']
print(multikeydict['z'])

try:
    print(multikeydict['x'])
except KeyError:
    print('Ключ отстутствует')

print("\n# TEST_3:")
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'y')
print(multikeydict['y'])

multikeydict['y'] += [30]
print(multikeydict['y'])

print("\n# TEST_4:")
multikeydict = MultiKeyDict(lecture='python', lesson='object oriented programming')

multikeydict.alias('lecture', 'lesson')
print(multikeydict['lesson'])

multikeydict.alias('lecture', 'lesson')
print(multikeydict['lesson'])

del multikeydict['lesson']
print(multikeydict['lesson'])

print("\n# TEST_5:")
mkey = MultiKeyDict(x=1)
mkey.alias('x', 'y')
mkey.alias('x', 'z')
print(mkey['x'], mkey['y'], mkey['z'])
mkey['x'] += 1
print(mkey['x'], mkey['y'], mkey['z'])

print("\n# TEST_6:")
mkey = MultiKeyDict(x=1)
mkey.alias('x', 'y')
mkey.alias('x', 'z')
print(mkey['x'], mkey['y'], mkey['z'])
mkey['y'] += 1
print(mkey['x'], mkey['y'], mkey['z'])

print("\n# TEST_7:")
multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])

print(multikeydict1['x'])
print(multikeydict1['y'])
print(multikeydict2['z'])

multikeydict1['a'] = 4
print(multikeydict1['a'])

print("\n# TEST_8:")
multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
multikeydict.alias('x', 't')
del multikeydict['x']
multikeydict['z'] += 1
print(multikeydict['z'])
print(multikeydict['t'])
