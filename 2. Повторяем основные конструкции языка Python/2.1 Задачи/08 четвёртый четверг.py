# Каждый месяц в Сан-Диего организовывается встреча любителей Python, которая проходит в четвертый четверг месяца.
#
# Напишите программу, которая определяет день проведения очередной встречи питонистов в Сан-Диего.
#
# Формат входных данных
# На вход программе подается два натуральных числа, представляющие год и месяц, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна определить день проведения встречи в Сан-Диего в указанных году и месяце и
# вывести результат в формате DD.MM.YYYY.

from calendar import monthcalendar
from datetime import date

year, month = int(input()), int(input())
this_month = monthcalendar(year, month)
this_date = this_month[3][3] if this_month[0][3] else this_month[4][3]
print(date(year, month, this_date).strftime('%d.%m.%Y'))
# можно было и не подгружать datetime
print(f'{this_date}.{month:02}.{year}')
