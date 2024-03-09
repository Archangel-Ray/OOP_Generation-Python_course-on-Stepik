"""
Реализуйте класс WeatherWarning, описывающий объект, предупреждающий о погодных изменениях.
    При создании экземпляра класс не должен принимать никаких аргументов.

Класс WeatherWarning должен иметь три метода экземпляра:

    rain() — метод, выводящий текст:

    Ожидаются сильные дожди и ливни с грозой

    snow() — метод, выводящий текст:

    Ожидается снег и усиление ветра

    low_temperature() — метод, выводящий текст:

    Ожидается сильное понижение температуры

Также реализуйте класс WeatherWarningWithDate, наследника класса WeatherWarning, описывающий объект,
    предупреждающий о погодных изменениях с указанием даты. Процесс создания экземпляра
    класса WeatherWarningWithDate должен совпадать с процессом создания экземпляра класса WeatherWarning.

Класс WeatherWarningWithDate должен иметь три метода экземпляра:

    rain() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:

    <дата в формате DD.MM.YYYY>
    Ожидаются сильные дожди и ливни с грозой

    snow() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:

    <дата в формате DD.MM.YYYY>
    Ожидается снег и усиление ветра

    low_temperature() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:

    <дата в формате DD.MM.YYYY>
    Ожидается сильное понижение температуры

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.
"""
from datetime import date


class WeatherWarning:
    @staticmethod
    def rain():
        print("Ожидаются сильные дожди и ливни с грозой")

    @staticmethod
    def snow():
        print("Ожидается снег и усиление ветра")

    @staticmethod
    def low_temperature():
        print("Ожидается сильное понижение температуры")


class WeatherWarningWithDate(WeatherWarning):
    @staticmethod
    def show(date_):
        print(date_.strftime('%d.%m.%Y'))

    def rain(self, date_):
        self.show(date_)
        super().rain()

    def snow(self, date_):
        self.show(date_)
        super().snow()

    def low_temperature(self, date_):
        self.show(date_)
        super().low_temperature()


# INPUT DATA:

# TEST_1:
print("\nтест 1")
print(issubclass(WeatherWarningWithDate, WeatherWarning))

# TEST_2:
print("\nтест 2")
weatherwarning = WeatherWarning()

weatherwarning.rain()
weatherwarning.snow()
weatherwarning.low_temperature()

# TEST_3:
print("\nтест 3")
weatherwarning = WeatherWarningWithDate()
dt = date(2022, 12, 12)

weatherwarning.rain(dt)
weatherwarning.snow(dt)
weatherwarning.low_temperature(dt)

# TEST_4:
print("\nтест 4")
weatherwarning = WeatherWarningWithDate()
dates = [date(2004, 6, 29), date(2012, 2, 1), date(1973, 2, 1), date(2020, 7, 8), date(2003, 2, 19), date(2022, 12, 25),
         date(2012, 8, 24), date(1977, 8, 5), date(2017, 5, 26), date(1976, 1, 8), date(2017, 11, 13), date(1989, 3, 4),
         date(1971, 12, 9), date(2011, 11, 13), date(1970, 6, 29), date(1983, 5, 11), date(1984, 8, 9),
         date(1999, 6, 15), date(2011, 3, 14), date(1980, 5, 26)]

for dt in dates:
    weatherwarning.rain(dt)
    weatherwarning.snow(dt)
    weatherwarning.low_temperature(dt)
