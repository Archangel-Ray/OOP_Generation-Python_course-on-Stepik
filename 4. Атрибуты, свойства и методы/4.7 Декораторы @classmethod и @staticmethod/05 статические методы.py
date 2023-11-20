"""
Реализуйте класс StrExtension, описывающий набор функций для работы со строками.
При создании экземпляра класс не должен принимать никаких аргументов.

Класс StrExtension должен иметь три статических метода:

    remove_vowels() — метод, который принимает в качестве аргумента строку, удаляет из нее все гласные
                       латинские буквы без учета регистра и возвращает полученный результат
    leave_alpha() — метод, который принимает в качестве аргумента строку, удаляет из нее все символы,
                     не являющиеся латинскими буквами, и возвращает полученный результат
    replace_all() — метод, который принимает три строковых аргумента string, chars и char, заменяет в строке
                     string все символы из chars на char с учетом регистра и возвращает полученный результат.

Примечание 1. Гарантируется, что все буквенные символы относятся к латинскому алфавиту.

Примечание 2. Латинские гласные буквы: a, e, i, o, u, y.

Примечание 3. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""
import string


class StrExtension:
    @staticmethod
    def remove_vowels(line: str):
        new_string = ""
        for let in line:
            if let.lower() not in "aeiouy":
                new_string += let
        return new_string

    @staticmethod
    def leave_alpha(line):
        new_string = ""
        for let in line:
            if let in string.ascii_letters:
                new_string += let
        return new_string

    @staticmethod
    def replace_all(line, chars, char):
        new_string = ""
        for let in line:
            if let in chars:
                new_string += char
            else:
                new_string += let
        return new_string


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))

# TEST_2:
print('\nтест 2')
print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))

# TEST_3:
print('\nтест 3')
print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))

# TEST_4:
print('\nтест 4')
print(StrExtension.remove_vowels('Success is the ability to go from failure to failure without losing your enthusiasm.'))
print(StrExtension.remove_vowels('Success is the ability to go from failure to failure without losing your enthusiasm.'.upper()))

# TEST_5:
print('\nтест 5')
print(StrExtension.leave_alpha('beegeek!\"#$%&\'()*+, -./:;<=>?@[\]^_`{|}~BEEGEEK'))
print(StrExtension.leave_alpha('beegeek0123456789BEEGEEK'))

# TEST_6:
print('\nтест 6')

text = '''I live in a house near the mountains. I have two brothers and one sister, and I was born last. My father teaches mathematics, and my mother is a nurse at a big hospital. My brothers are very smart and work hard in school. My sister is a nervous girl, but she is very kind. My grandmother also lives with us. She came from Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food!
My family is very important to me. We do lots of things together. My brothers and I like to go on long walks in the mountains. My sister likes to cook with my grandmother. On the weekends we all play board games together. We laugh and always have a good time. I love my family very much.'''

print(StrExtension.remove_vowels(text))
print(StrExtension.leave_alpha(text))
print(StrExtension.replace_all(text, string.ascii_lowercase, ''))
