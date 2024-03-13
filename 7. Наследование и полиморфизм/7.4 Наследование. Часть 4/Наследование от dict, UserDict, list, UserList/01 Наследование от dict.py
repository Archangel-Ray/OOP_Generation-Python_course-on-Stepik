"""
Создадим класс UpperCaseDict, наследника класса dict, который автоматически сохраняет все ключи в виде строк, 
    в которых все буквы будут в верхнем регистре.
Для реализации класса UpperCaseDict необходимо переопределить все методы, например:
 __setitem__(), update(), __init__(), setdefault()
"""


class UpperCaseDict(dict):
    def __init__(self, items=(), **kwargs):
        self.update(items)
        self.update(kwargs)

    def update(self, items):
        if isinstance(items, dict):
            items = items.items()
        for key, value in items:
            self[key] = value

    def setdefault(self, key, value):
        if str(key).upper() not in self:
            self[key] = value

    def __setitem__(self, key, value):
        key = str(key).upper()
        super().__setitem__(key, value)

    def __repr__(self):
        return f'{type(self).__name__}({super().__repr__()})'


numbers = UpperCaseDict()
numbers['one'] = 1
numbers['two'] = 2

numbers.update({'three': 3})
print(numbers)

numbers = UpperCaseDict(one=1, two=2, three=3)
print(numbers)

numbers = UpperCaseDict()
numbers.setdefault('one', 1)
print(numbers)
