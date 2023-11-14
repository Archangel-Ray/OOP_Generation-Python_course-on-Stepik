"""
Будем называть словом любую последовательность из одной или более латинских букв.

Реализуйте класс Wordplay, описывающий расширяемый набор слов.
При создании экземпляра класс должен принимать один аргумент:

    words — список, определяющий начальный набор слов. Если не передан, начальный набор слов считается пустым

Экземпляр класса Wordplay должен иметь один атрибут:

    words — список, содержащий набор слов

Класс Wordplay должен иметь четыре метода экземпляра:

    add_word() — метод, принимающий в качестве аргумента слово и добавляющий его в набор.
                  Если слово уже есть в наборе, метод ничего не должен делать
    words_with_length() — метод, принимающий в качестве аргумента натуральное число n и
                           возвращающий список слов из набора, длина которых равна n
    only() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из набора,
              которые включают в себя только переданные буквы
    avoid() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из списка words,
               которые не содержат ни одну из этих букв

Примечание 1. Слова в списках, возвращаемых методами words_with_length(), only() и avoid(),
должны располагаться в том порядке, в котором они были добавлены.

Примечание 2. Экземпляр класса Wordplay не должен зависеть от списка, на основе которого он был создан.
Другими словами, если исходный список изменится, то экземпляр класса Wordplay измениться не должен.

Примечание 3. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Wordplay:
    def __init__(self, new_dict=None):
        if new_dict is None:
            self.words = list()
        else:
            self.words = new_dict[:]

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, num):
        list_words = list()
        for word in self.words:
            if len(word) == num:
                list_words.append(word)
        return list_words

    def only(self, *args):
        list_words = list()
        for word in self.words:
            if not set(word).difference(set(args)):
                list_words.append(word)
        return list_words

    def avoid(self, *args):
        list_words = list()
        for word in self.words:
            if not set(word).intersection(set(args)):
                list_words.append(word)
        return list_words


# INPUT DATA:

# TEST_1:
wordplay = Wordplay()

print(wordplay.words_with_length(1))
print(wordplay.only('a', 'b', 'c'))
print(wordplay.avoid('a', 'b', 'c'))

# TEST_2:
wordplay = Wordplay()

print(wordplay.words)
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)

# TEST_3:
wordplay = Wordplay(['bee', 'geek', 'cool', 'stepik'])

wordplay.add_word('python')
print(wordplay.words_with_length(4))

# TEST_4:
wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

print(wordplay.only('o', 't'))

# TEST_5:
wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.avoid('a', 'b', 'c'))

# TEST_6:
wordplay = Wordplay()
print(wordplay.words)

# TEST_7:
wordplay = Wordplay(['Тьюринг', 'Торвальдс', 'Россум', 'Гейтс', 'Гамильтон', 'Бэкус', 'Кнут'])

print(wordplay.words_with_length(6))
print(wordplay.avoid('ь'))

# TEST_8:
words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)

# TEST_9:
wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.words)
wordplay.add_word('stepik')
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)
