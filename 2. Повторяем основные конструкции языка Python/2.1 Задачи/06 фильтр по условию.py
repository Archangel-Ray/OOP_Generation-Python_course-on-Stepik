# Географические координаты представляют собой пару чисел (x,y)(x,y), где xx — широта, yy — долгота,
# причем −90°≤x≤90°−90°≤x≤90°, −180°≤y≤180°−180°≤y≤180°.
#
# Напишите программу, которая принимает произвольное количество строк и определяет,
# какие из них представляют собой корректные географические координаты.
#
# Формат входных данных
# На вход программе подается произвольное количество строк,
# каждая из которых представляет собой пару чисел в следующем формате:
#
# (<координата x>, <координата y>)
#
# Формат выходных данных
# Программа должна для каждой строки вывести True, если она представляет собой корректные географические координаты,
# или False в противном случае.

list_coord = open(0).readlines()
for x_y in list_coord:
    x, y = x_y.strip().split(', ')
    print(-90 <= float(x.strip('(')) <= 90 and -180 <= float(y.strip(')')) <= 180)
