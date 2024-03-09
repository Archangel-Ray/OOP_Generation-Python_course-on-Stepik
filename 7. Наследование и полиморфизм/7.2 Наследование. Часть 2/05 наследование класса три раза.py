"""
1. Реализуйте класс Summator, описывающий объект, вычисляющий сумму натуральных чисел от 1 до n:
1+2+3+...+n
При создании экземпляра класс не должен принимать никаких аргументов.

Класс Summator должен иметь один метод экземпляра:

    total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму целых чисел
                от 1 до n включительно

2. Помимо этого, реализуйте класс SquareSummator, наследника класса Summator, описывающий объект,
    вычисляющий сумму квадратов натуральных чисел от 1 до n:
12+22+32+...+n2
Процесс создания экземпляра класса SquareSummator должен совпадать с процессом создания экземпляра класса Summator.

Класс SquareSummator должен иметь один метод экземпляра:

    total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму квадратов целых чисел
                от 1 до n включительно

3. Также реализуйте класс QubeSummator, наследника класса Summator, описывающий объект, вычисляющий сумму кубов
    натуральных чисел от 1 до n:
13+23+33+...+n3

Процесс создания экземпляра класса QubeSummator должен совпадать с процессом создания экземпляра класса Summator.

Класс QubeSummator должен иметь один метод экземпляра:

    total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму кубов целых чисел
                от 1 до n включительно

4. Наконец, реализуйте класс CustomSummator, наследника класса Summator, описывающий объект, вычисляющий сумму
    произвольных степеней натуральных чисел от 1 до n:
1m+2m+3m+...+nm

При создании экземпляра класс должен принимать один аргумент:

    m — степень чисел в последовательности

Класс CustomSummator должен иметь один метод экземпляра:

    total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму целых чисел в степени m
                от 1 до n включительно

Примечание 1. Попытайтесь реализовать классы таким образом, чтобы метод total() был определен лишь в классе Summator.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации классов нет, она может быть произвольной.
"""


class Summator:
    def total(self, n, m=1):
        if n:
            answer = n ** m + self.total(n - 1, m)
            return answer
        return 0


class SquareSummator(Summator):
    def total(self, n, m=1):
        return super().total(n, 2)


class QubeSummator(Summator):
    def total(self, n, m=1):
        return super().total(n, 3)


class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

    def total(self, n, m=1):
        return super().total(n, self.m)


# INPUT DATA:

# TEST_1:
print("\nтест 1")
print(issubclass(SquareSummator, Summator))
print(issubclass(QubeSummator, Summator))

# TEST_2:
print("\nтест 2")
summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))  # 1 + 2 + 3
print(summator2.total(3))  # 1 + 4 + 9
print(summator3.total(3))  # 1 + 8 + 27

# TEST_3:
print("\nтест 3")
summator1 = Summator()
summator2 = CustomSummator(2)
summator3 = CustomSummator(3)

print(summator1.total(3))  # 1 + 2 + 3
print(summator2.total(3))  # 1 + 4 + 9
print(summator3.total(3))  # 1 + 8 + 27

# TEST_4:
print("\nтест 4")
summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

for i in range(5, 50):
    print(summator1.total(i), summator2.total(i), summator3.total(i))

# TEST_5:
print("\nтест 5")
for i in range(5, 50):
    summator = CustomSummator(i)
    print(summator.total(10))
