"""
Класс UserDict – это удобная обертка для обычного объекта dict. Этот класс обеспечивает то же поведение, что и dict, 
    с дополнительной возможностью предоставления доступа к базовому словарю через атрибут экземпляра data.  
    Нет необходимости предоставлять собственные реализации методов __init__(), update() и setdefault(). 
    Это связано с тем, что в UserDict все методы, обновляющие существующие ключи или добавляющие новые, 
    полагаются на пользовательскую версию метода __setitem__().
"""
from collections import UserDict


class UpperCaseDict(UserDict):
    def __setitem__(self, key, value):
        key = str(key).upper()
        self.data.__setitem__(key, value)
    
    def __repr__(self):
        return f'{type(self).__name__}({self.data.__repr__()})'


numbers = UpperCaseDict({'one': 1, 'two': 2})

numbers['three'] = 3
numbers.update({'four': 4})
numbers.setdefault('five', 5)

print(numbers)
