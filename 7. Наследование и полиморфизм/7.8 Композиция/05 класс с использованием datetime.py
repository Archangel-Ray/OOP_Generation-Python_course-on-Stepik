"""
1. Реализуйте класс Lecture, описывающий некоторое выступление. При создании экземпляра класс должен принимать
    три аргумента в следующем порядке:

    topic — тема выступления
    start_time — время начала выступления в виде строки в формате HH:MM
    duration — длительность выступления в виде строки в формате HH:MM

2. Также реализуйте класс Conference, описывающий конференцию, протяженностью в один день. Конференция представляет
    собой набор последовательных выступлений. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Conference должен иметь четыре метода экземпляра:

    add() — метод, принимающий в качестве аргумента выступление и добавляющий его в конференцию. Если выступление
            пересекается по времени с другими выступлениями, должно быть возбуждено исключение ValueError с текстом:

            Провести выступление в это время невозможно

    total() — метод, возвращающий суммарную длительность всех выступлений в конференции в виде строки в формате HH:MM
    longest_lecture() — метод, возвращающий длительность самого долгого выступления в конференции в виде строки
                        в формате HH:MM
    longest_break() — метод, возвращающий длительность самого долгого перерыва между выступлениями в конференции
                        в виде строки в формате HH:MM

Примечание 1. Перерыв между выступлениями может быть нулевым. Другими словами, одно выступление может заканчиваться,
                например, в 12:00, а другое начинаться в 12:00.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
"""
from datetime import timedelta, datetime


class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = datetime.strptime(start_time, "%H:%M")
        hours, minutes = map(int, duration.split(":"))
        self.duration = timedelta(hours=hours, minutes=minutes)
        self.ending = self.start_time + self.duration

    def __lt__(self, other):
        return self.start_time < other.start_time


class Conference:
    def __init__(self):
        self.conference = []

    @staticmethod
    def check(on_schedule, current):
        if on_schedule.start_time < current.start_time < on_schedule.ending \
                or on_schedule.start_time < current.ending < on_schedule.ending\
                or current.start_time < on_schedule.start_time < current.ending\
                or current.start_time == on_schedule.start_time:
            raise ValueError("Провести выступление в это время невозможно")

    @staticmethod
    def converter(segment):
        return f"{segment.seconds // (60 * 60):02}:{segment.seconds // 60 % 60:02}"

    def add(self, lecture):
        for lecture_at in self.conference:
            self.check(lecture_at, lecture)
        self.conference.append(lecture)

    def total(self):
        all_gaps = self.conference[0].duration
        for i in range(1, len(self.conference)):
            all_gaps += self.conference[i].duration
        return self.converter(all_gaps)

    def longest_lecture(self):
        longest = max([x.duration for x in self.conference])
        for lecture in self.conference:
            if lecture.duration == longest:
                return self.converter(lecture.duration)

    def longest_break(self):
        gaps = []
        sorted_conference = sorted(self.conference)
        if len(self.conference) > 1:
            for i in range(1, len(sorted_conference)):
                if sorted_conference[i].start_time != sorted_conference[i - 1].ending:
                    gaps.append(sorted_conference[i].start_time - sorted_conference[i - 1].ending)
        if gaps:
            gaps = max(gaps)
            return self.converter(gaps)
        else:
            return self.converter(timedelta(seconds=0))


# INPUT DATA:

print("\n# TEST_1:")
conference = Conference()

conference.add(Lecture('Простые числа', '08:00', '01:30'))
conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))
conference.add(Lecture('Муравьиный алгоритм', '13:30', '01:50'))
print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())

print("\n# TEST_2:")
conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:30'))

try:
    conference.add(Lecture('Жизнь после ChatGPT', '09:00', '02:00'))
except ValueError as error:
    print(error)

print("\n# TEST_3:")
conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:00'))
conference.add(Lecture('Жизнь после ChatGPT', '11:00', '02:00'))

try:
    conference.add(Lecture('Муравьиный алгоритм', '10:00', '04:00'))
except ValueError as error:
    print(error)

print("\n# TEST_4:")
conference = Conference()
conference.add(Lecture('Муравьиный алгоритм', '09:30', '02:00'))
conference.add(Lecture('Жизнь после ChatGPT', '11:45', '04:00'))
conference.add(Lecture('Простые числа', '08:00', '01:30'))

print(conference.longest_lecture())
print(conference.longest_break())

print("\n# TEST_5:")
conference = Conference()
conference.add(Lecture('Введение в ООП', '09:30', '00:30'))
conference.add(Lecture('Атрибуты объектов и классов', '08:00', '01:30'))
conference.add(Lecture('Методы экземляра класса', '10:30', '02:00'))

print(conference.longest_lecture())
print(conference.longest_break())

print("\n# TEST_6:")
conference = Conference()
conference.add(Lecture('Декоратор @property', '09:30', '00:30'))
conference.add(Lecture('Свойства', '09:00', '00:30'))
conference.add(Lecture('Модификаторы доступа и аксессоры', '08:30', '00:30'))

print(conference.longest_lecture())
print(conference.longest_break())

print("\n# TEST_7:")
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))

try:
    conference.add(Lecture('Декоратор @singledispatchmethod', '09:30', '00:30'))
except ValueError as e:
    print(e)

print("\n# TEST_8:")
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))

try:
    conference.add(Lecture('Декоратор @singledispatchmethod', '09:45', '00:30'))
except ValueError as e:
    print(e)

print("\n# TEST_9:")
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))

try:
    conference.add(Lecture('Декоратор @singledispatchmethod', '09:59', '00:30'))
except ValueError as e:
    print(e)

print("\n# TEST_10:")
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))

try:
    conference.add(Lecture('Декоратор @singledispatchmethod', '09:00', '00:35'))
except ValueError as e:
    print(e)

print("\n# TEST_11:")
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))
conference.add(Lecture('Декоратор @singledispatchmethod', '09:00', '00:30'))
conference.add(Lecture('Создание, инициализация и очищение объектов', '11:00', '00:30'))

start_times = ['09:30', '09:45', '09:59', '09:00', '09:00', '09:15', '09:29', '08:30', '11:00', '11:15', '11:25',
               '10:45']
durations = ['00:30', '00:30', '00:30', '00:35', '00:15', '00:15', '00:30', '00:35', '00:20', '00:10', '00:35', '00:16']

for start_time_, duration_ in zip(start_times, durations):
    try:
        conference.add(Lecture('Строковое представление объектов', start_time_, duration_))
    except ValueError as e:
        print(e)

print("\n# TEST_12:")
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))
conference.add(Lecture('Декоратор @singledispatchmethod', '09:00', '00:30'))
conference.add(Lecture('Создание, инициализация и очищение объектов', '11:00', '00:30'))
conference.add(Lecture('Унарные операторы и функции', '10:45', '00:15'))
conference.add(Lecture('Арифметические операции', '10:00', '00:30'))
conference.add(Lecture('Вызываемые объекты', '08:00', '01:00'))

print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())
