"""
Реализуйте класс ReadableTextFile. При создании экземпляра класс должен принимать один аргумент:

    filename — имя текстового файла

Экземпляр класса ReadableTextFile должен являться контекстным менеджером, который открывает файл с именем filename
    на чтение в кодировке UTF-8 и позволяет получать его строки без символа переноса строки \n на конце.
    Также контекстный менеджер должен закрывать открытый им файл после выполнения кода внутри блока with.

Примечание 1. Наглядные примеры использования класса ReadableTextFile продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
                используется только с корректными данными.

Примечание 3. Класс ReadableTextFile должен удовлетворять протоколу контекстного менеджера,
                то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.
"""


class ReadableTextFile:
    def __init__(self, filename):
        self.file = open(filename, encoding="utf-8")

    def __enter__(self):
        return (row.rstrip() for row in self.file.readlines())

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# INPUT DATA:

# TEST_1:
print('\nтест 1')
with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
    print('Только посмотрите!', file=file)
    print('Как величаво она парит в воздухе', file=file)
    print('Как орел', file=file)
    print('На воздушном шаре', file=file)

with ReadableTextFile('glados_quotes.txt') as file:
    for line in file:
        print(line)

# TEST_2:
print('\nтест 2')
with open('poem.txt', 'w', encoding='utf-8') as file:
    print('Я кашлянул в звенящей тишине,', file=file)
    print('И от шального эха стало жутко…', file=file)
    print('Расскажет ли утятам обо мне', file=file)
    print('под утро мной испуганная утка?', file=file)

with ReadableTextFile('poem.txt') as file:
    for line in file:
        print(line)

# TEST_3:
print('\nтест 3')
text = '''Измученный дорогой, я выбился из сил,
И в доме лесника я ночлега попросил.
С улыбкой добродушной старик меня впустил,
И жестом дружелюбным на ужин пригласил.

Будь как дома путник, я ни в чем не откажу,
Я ни в чем не откажу, я ни в чем не откажу!
Множество историй, коль желаешь расскажу,
Коль желаешь расскажу, коль желаешь расскажу!

На улице темнело, сидел я за столом.
Лесник сидел напротив, болтал о том, о сем.
Что нет среди животных у старика врагов,
Что нравится ему подкармливать волков.

Будь как дома путник, я ни в чем не откажу,
Я ни в чем не откажу, я ни в чем не откажу!
Множество историй, коль желаешь расскажу,
Коль желаешь расскажу, коль желаешь расскажу!

И волки среди ночи завыли под окном.
Старик заулыбался и вдруг покинул дом.
Но вскоре возвратился с ружьем на перевес:
Друзья хотят покушать, пойдем приятель в лес!

Будь как дома путник, я ни в чем не откажу,
Я ни в чем не откажу, я ни в чем не откажу!
Множество историй, коль желаешь расскажу,
Коль желаешь расскажу, коль желаешь расскажу!'''

with open('forester.txt', 'w', encoding='utf-8') as file:
    file.write(text)

with ReadableTextFile('forester.txt') as file:
    for line in file:
        print(line)

# TEST_4:
print('\nтест 4')
text = '''Dog goes woof, cat goes meow
Bird goes tweet and mouse goes squeak
Cow goes moo, the frog goes croak
and the elephant goes toot

Ducks say quack and fish go blub
and the seal goes ow, ow, ow
But there’s one sound that no one knows

What does the fox say?

Ring-ding-ding-ding-dingeringeding!
Gering-ding-ding-ding-dingeringeding!
Gering-ding-ding-ding-dingeringeding!

What the fox say?

Wa-pa-pa-pa-pa-pa-pow!
Wa-pa-pa-pa-pa-pa-pow!
Wa-pa-pa-pa-pa-pa-pow!
What the fox say?

Ha-tee-ha-tee-ha-tee-ho!
Hatee-hatee-ha-tee-ho!
Ha-tee-hatee-hatee-ho!
What the fox say?

Joff-tchoff-tchoffo-tchoffo-tchoff!
Tchoff-tchoff-tchoffo-tchoffo-tchoff!
Joff-tchoff-tchoffo-tchoffo-tchoff!

What the fox say?

Big blue eyes, pointy nose
Chasing mice and digging holes
Tiny paws, up the hill
Suddenly you’re standing still

Your fur is red, so beautiful
Like an angel in disguise
But if you meet a friendly horse
Will you communicate by
mo-o-o-o-orse?
mo-o-o-o-orse?
mo-o-o-o-orse?

How will you speak to that
ho-o-o-o-orse?
ho-o-o-o-orse?
ho-o-o-o-orse?

What does the fox say?

Jacha-chacha-chacha-chow!
Chacha-chacha-chacha-chow!
Chacha-chacha-chacha-chow!

What the fox say?

Fraka-kaka-kaka-kaka-kow!
Fraka-kaka-kaka-kaka-kow!
Fraka-kaka-kaka-kaka-kow!

What the fox say?

A-hee-ahee ha-hee!
A-hee-ahee ha-hee!
A-hee-ahee ha-hee!

What the fox say?

A-oo-oo-oo-ooo!
Woo-oo-oo-ooo!

What does the fox say?

The secret of the fox, ancient mystery
Somewhere deep in the woods I know you’re hiding
What is your sound? Will we ever know?
Will always be a mystery, what do you say?
You’re my guardian angel, hiding in the woods
What is your sound?'''

with open('fox.txt', 'w', encoding='utf-8') as file:
    file.write(text)

with ReadableTextFile('fox.txt') as file:
    for line in file:
        print(line)

# TEST_5:
print('\nтест 5')
text = ''

with open('empty.txt', 'w', encoding='utf-8') as file:
    file.write(text)

with ReadableTextFile('empty.txt') as file:
    for line in file:
        print(line)
