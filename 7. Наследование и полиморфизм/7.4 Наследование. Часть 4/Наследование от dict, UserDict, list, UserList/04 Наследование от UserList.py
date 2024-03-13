"""
Класс UserList – это удобная обертка для обычного объекта list. Этот класс обеспечивает то же поведение, что list, с дополнительной возможностью предоставления доступа к базовому списку через атрибут экземпляра data.
Наследники класса UserList должны предоставить инициализатор, который можно вызывать либо без аргументов, либо с одним аргументом, определяющим начальный набор элементов.
Если есть необходимость, чтобы класс StringList поддерживал конкатенацию с помощью оператора плюс +, то потребуется реализовать магические методы __add__(), __radd__() и __iadd__().
"""
from collections import UserList


class StringList(UserList):
    def __init__(self, iterable):
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        self.data[index] = str(item)

    def insert(self, index, item):
        self.data.insert(index, str(item))

    def append(self, item):
        self.data.append(str(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(str(item) for item in other)

    def __repr__(self):
        return f'{type(self).__name__}({self.data.__repr__()})'


lst = StringList([1, 2, 3])

lst[2] = 4
lst.append(5)
lst.insert(0, 6)
lst.extend([6, 7, 8])

print(lst)
