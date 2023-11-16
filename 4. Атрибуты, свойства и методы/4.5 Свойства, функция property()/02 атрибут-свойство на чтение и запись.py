"""
Реализуйте класс HourClock, описывающий часы с одной лишь часовой стрелкой.
При создании экземпляра класс должен принимать один аргумент:

    hours — количество часов. Если hours не является целым числом, принадлежащим диапазону [1; 12],
             должно быть возбуждено исключение ValueError с текстом:

             Некорректное время

Класс HourClock должен иметь одно свойство:

    hours — свойство, доступное для чтения и записи, возвращающее текущее количество часов.
             При изменении свойство должно проверять, что новое значение является целым числом,
             принадлежащим диапазону [1; 12], в противном случае должно быть возбуждено
             исключение ValueError с текстом:

             Некорректное время

Примечание 1. Никаких ограничений касательно реализации класса HourClock нет, она может быть произвольной.
"""


class HourClock:
    def __init__(self, hours):
        self._hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if type(hours) is int and 1 <= hours <= 12:
            self._hours = hours
        else:
            raise ValueError('Некорректное время')

    _hours = property(get_hours, set_hours)


# INPUT DATA:

# TEST_1:
time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)

# TEST_2:
time = HourClock(7)

try:
    time.hours = 15
except ValueError as e:
    print(e)

# TEST_3:
try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)

# TEST_4:
try:
    HourClock(0)
except ValueError as e:
    print(e)

# TEST_5:
try:
    HourClock('ten o`clock')
except ValueError as e:
    print(e)

# TEST_6:
time = HourClock(1)

print(time.hours)
for _ in range(11):
    time.hours += 1
    print(time.hours)

# TEST_7:
time = HourClock(1)
print(hasattr(HourClock, 'hours'))
