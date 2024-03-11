"""
Реализуйте класс TitledText, наследника класса str, который описывает текст, имеющий заголовок. При создании
    экземпляра класс должен принимать два аргумента в следующем порядке:

    content — текст
    text_title — заголовок текста

Класс TitledText должен иметь один метод экземпляра:

    title() — метод, возвращающий заголовок текста

Примечание 1. Значением экземпляра класса TitledText должен быть именно текст,
                а не заголовок текста или текст вместе с заголовком.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса TitledText нет, она может быть произвольной.
"""


class TitledText(str):
    def __new__(cls, content_, text_title):
        obj = super().__new__(cls, content_)
        obj.text_title = text_title
        return obj

    def title(self):
        return self.text_title


# INPUT DATA:

# TEST_1:
print("\nтест 1")
titled = TitledText('Сreate a class Soda', 'Homework')

print(titled)
print(titled.title())
print(issubclass(TitledText, str))

# TEST_2:
print("\nтест 2")
titled1 = TitledText('Сreate a class Soda', 'Homework')
titled2 = TitledText('Сreate a class Soda', 'Exam')

print(titled1 == titled2)

# TEST_3:
print("\nтест 3")
headlines = ['Как полностью изменить...', 'Где найти …', 'Быстрый способ...', 'Ошибки, которые приведут тебя к ...',
             'Как быстро...']
contents = ['Нужно всего лишь...', 'Обратитесь к нам, и мы всё расскажем', 'Для этого Вы должны', 'Не делай их',
            'Ну это вообще просто']

for heading, content in zip(headlines, contents):
    titledtext = TitledText(content, heading)
    print(titledtext.title(), titledtext)
