"""
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_)
и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.

Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов,
при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case.
При создании экземпляра класс не должен принимать никаких аргументов.

Класс CaseHelper должен иметь четыре статических метода:

    is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True,
                  если переданная строка записана в стиле Snake Case, или False в противном случае
    is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True,
                        если переданная строка записана в стиле Upper Camel Case, или False в противном случае
    to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case,
                  записывает ее в стиле Snake Case и возвращает полученный результат
    to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case,
                        записывает ее в стиле Upper Camel Case и возвращает полученный результат
"""


class CaseHelper:
    @staticmethod
    def is_snake(line: str):
        return True if line == line.lower() and " " not in line and "__" not in line else False

    @staticmethod
    def is_upper_camel(line: str):
        return True if line[0] == line[0].upper() and " " not in line and "_" not in line else False

    @staticmethod
    def to_snake(line: str):
        new_line = ""
        for letter in line:
            if letter == letter.upper():
                new_line += " "
                new_line += letter.lower()
            else:
                new_line += letter.lower()
        return "_".join(new_line.split())

    @staticmethod
    def to_upper_camel(line: str):
        return "".join(map(str.capitalize, line.split("_")))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))

# TEST_2:
print('\nтест 2')
print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))

# TEST_3:
print('\nтест 3')
print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))

# TEST_4:
print('\nтест 4')
print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))

# TEST_5:
print('\nтест 5')
cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup']

for case in cases:
    print(CaseHelper.is_snake(case))

# TEST_6:
print('\nтест 6')
cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp',
         'tearDown', 'run', 'exit', 'setup', 'AssertEqual', 'SetUp']

for case in cases:
    print(CaseHelper.is_upper_camel(case))

# TEST_7:
print('\nтест 7')
cases = ['AssertEqual', 'SetUp', 'TearDown', 'AddModuleCleanup', 'AssertRaisesRegex',
         'AssertAlmostEqual', 'AssertNotAlmostEqual']

for case in cases:
    print(CaseHelper.to_snake(case))

# TEST_8:
print('\nтест 8')
cases = ['assert_equal', 'tear_down', 'assert_raises_regex', 'assert_almost_equal',
         'assert_not_almost_equal', 'beegeek']

for case in cases:
    print(CaseHelper.to_upper_camel(case))

# TEST_9:
print('\nтест 9')
obj = CaseHelper()
print(type(obj.is_snake))
print(type(obj.is_upper_camel))
print(type(obj.to_snake))
print(type(obj.to_upper_camel))
