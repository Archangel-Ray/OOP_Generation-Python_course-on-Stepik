"""
1. Реализуйте класс Weekday, описывающий перечисление с днями недели. Перечисление должно иметь семь элементов:

    MONDAY — элемент со значением 0
    TUESDAY — элемент со значением 1
    WEDNESDAY — элемент со значением 2
    THURSDAY — элемент со значением 3
    FRIDAY — элемент со значением 4
    SATURDAY — элемент со значением 5
    SUNDAY — элемент со значением 6

2. Также реализуйте класс NextDate, позволяющий определять дату следующего дня недели, начиная с текущего дня.
    При создании экземпляра класс должен принимать три аргумента в следующем порядке:

    today — дата текущего дня, представленная экземпляром класса date
    weekday — день недели, представленный элементом перечисления Weekday
    after_today — булево значение, по умолчанию равняется False

Параметр after_today должен определять, учитывается ли текущая дата при определении даты следующего дня недели.
    Если он имеет значение False, текущая дата не должна учитываться, если True — должна учитываться.

Класс NextDate должен иметь два метода экземпляра:

    date() — метод, возвращающий дату следующего дня недели в виде экземпляра класса date
    days_until() — метод, возвращающий количество дней до даты следующего дня недели

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
"""
from datetime import date, timedelta
from enum import Enum


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today
        self.date_next_weekday = today if after_today else today + timedelta(days=1)

    def date(self):
        while self.date_next_weekday.strftime("%A").upper() != self.weekday.name:
            self.date_next_weekday += timedelta(days=1)
        return self.date_next_weekday

    def days_until(self):
        return (self.date_next_weekday - self.today).days


# INPUT DATA:

print("\n# TEST_1:")
today_ = date(2023, 4, 17)  # понедельник
next_friday = NextDate(today_, Weekday.FRIDAY)  # следующая пятница

print(next_friday.date())
print(next_friday.days_until())

print("\n# TEST_2:")
today_ = date(2023, 4, 17)  # понедельник
next_monday = NextDate(today_, Weekday.MONDAY)  # следующий понедельник без учета текущего

print(next_monday.date())
print(next_monday.days_until())

print("\n# TEST_3:")
today_ = date(2023, 4, 17)  # понедельник
next_monday = NextDate(today_, Weekday.MONDAY, True)  # следующий понедельник с учетом текущего

print(next_monday.date())
print(next_monday.days_until())

print("\n# TEST_4:")
for weekday_ in Weekday:
    today_ = date(2023, 4, 27)  # четверг
    next_date = NextDate(today_, weekday_)

    print(next_date.date())
    print(next_date.days_until())

print("\n# TEST_5:")
for weekday_ in Weekday:
    today_ = date(2023, 4, 27)  # четверг
    next_date = NextDate(today_, weekday_, True)

    print(next_date.date())
    print(next_date.days_until())

print("\n# TEST_6:")
today_ = date(2023, 4, 23)

for _ in range(7):
    today_ += timedelta(days=1)
    for weekday_ in Weekday:
        next_date = NextDate(today_, weekday_)
        print(f'Today = {today_} {Weekday(today_.weekday()).name}, next {weekday_.name} = {next_date.date()}')
        print(f'Days until = {next_date.days_until()}')

print("\n# TEST_7:")
today_ = date(2023, 4, 23)

for _ in range(7):
    today_ += timedelta(days=1)
    for weekday_ in Weekday:
        next_date = NextDate(today_, weekday_, True)
        print(f'Today = {today_} {Weekday(today_.weekday()).name}, next {weekday_.name} = {next_date.date()}')
        print(f'Days until = {next_date.days_until()}')
