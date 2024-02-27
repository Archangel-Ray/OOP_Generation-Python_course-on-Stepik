"""
Реализуйте функцию print_file_content(), которая принимает один аргумент:

    filename — имя текстового файла

Функция должна выводить содержимое файла с именем filename. Если файла с данным именем нет в папке с программой,
    функция должна вывести текст:

    Файл не найден

Примечание 1. Имя файла, передаваемого в функцию, уже содержит расширение.

Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.
"""


def print_file_content(filename):
    try:
        with open(filename, encoding='utf-8') as file_:
            for row in file_.readlines():
                print(row.strip())
    except FileNotFoundError:
        print("Файл не найден")


# INPUT DATA:

# TEST_1:
with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
    file.write('Сражения и путешествия берут своё')

print_file_content('Precepts_of_Zote.txt')

# TEST_2:
print_file_content('Precepts_of_Zote2.txt')

# TEST_3:
with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
    print('Сражения и путешествия берут своё', file=file)
    print('Во время отдыха твоё тело становится сильнее, а раны заживают', file=file)
    print('Чем больше отдыхаешь, тем сильнее становишься', file=file)

print_file_content('Precepts_of_Zote.txt')

# TEST_4:
print_file_content('missing_file.txt')

# TEST_5:
with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
    file.writelines(
        ['Сражения и путешествия берут своё\n', 'Во время отдыха твоё тело становится сильнее, а раны заживают'])

print_file_content('Precepts_of_Zote.txt')
