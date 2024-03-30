"""
Реализуйте класс исключений DomainException. Также реализуйте класс Domain для работы с доменами. Класс Domain должен
    поддерживать три способа создания своего экземпляра: напрямую через вызов класса, а также с помощью двух методов
    класса from_url() и from_email():

    domain1 = Domain('pygen.ru')                       # непосредственно на основе домена
    domain2 = Domain.from_url('https://pygen.ru')      # на основе url-адреса
    domain3 = Domain.from_email('support@pygen.ru')    # на основе адреса электронной почты

При попытке создания экземпляра класса Domain на основе некорректных домена, url-адреса или адреса электронной почты
    должно быть возбуждено исключение DomainException с текстом:

    Недопустимый домен, url или email

В качестве неформального строкового представления экземпляр класса Domain должен иметь собственный домен:

    print(str(domain1))                                # pygen.ru
    print(str(domain2))                                # pygen.ru
    print(str(domain3))                                # pygen.ru

Примечание 1. Будем считать домен корректным, если он представляет собой последовательность из одной или более
              латинских букв, за которой следует точка, а затем снова одна или более латинских букв.

Примечание 2. Будем считать url-адрес корректным, если он представляет собой строку http:// или https://,
              за которой следует корректный домен.

Примечание 3. Будем считать адрес электронной почты корректным, если он представляет собой последовательность
              из одной или более латинских букв, за которой следует собачка (@), а затем корректный домен.
"""
from re import search


class DomainException(Exception):
    def __str__(self):
        return "Недопустимый домен, url или email"


class Domain:
    def __init__(self, address):
        self.address = self.check(address)

    @classmethod
    def check(cls, text):
        if search(r"^(http://|https://)(\w+[.]\w+$)", text):
            return search(r"^(http://|https://)(\w+[.]\w+$)", text)[2]
        if "@" in text:
            if search(r"^[a-zA-Z]+@(\w+[.]\w+$)", text):
                return search(r"^[a-zA-Z]+@(\w+[.]\w+$)", text)[1]
        if search(r"^(\w+[.]\w+$)", text):
            return text
        raise DomainException

    @classmethod
    def from_url(cls, text):
        return cls(text)

    @classmethod
    def from_email(cls, text):
        return cls(text)

    def __str__(self):
        return str(self.address)


# INPUT DATA:

print("\n# TEST_1:")
domain1 = Domain('pygen.ru')
domain2 = Domain.from_url('https://pygen.ru')
domain3 = Domain.from_email('support@pygen.ru')

print(domain1)
print(domain2)
print(domain3)

print("\n# TEST_2:")
try:
    domain1 = Domain('pygen..org')
except DomainException as e:
    print(e)

print("\n# TEST_3:")
domain1 = Domain('stepik.org')
domain2 = Domain.from_url('https://stepik.org')
domain3 = Domain.from_email('support@stepik.org')

print(domain1)
print(domain2)
print(domain3)

print("\n# TEST_4:")
domains = ['ip.ru', 'ao.org', 'npo.com', 'npo.com', 'zao.org', 'sibtred.info', 'ao.biz', 'npo.net', 'npo.net',
           'oao.net', 'zao.com', 'pahomov.org', 'bikova.ru', 'ooo.ru', 'transol.net', 'zao.com', 'rao.info', 'ooo.org',
           'krjukov.com', 'nikonova.com']

for d in domains:
    domain = Domain(d)
    print(domain)

print("\n# TEST_5:")
emails = ['maksim@hotmail.com', 'pavel@hotmail.com', 'taisija@hotmail.com', 'elizar@mail.ru',
          'olimpiada@mail.ru', 'alla@hotmail.com', 'fomichevagap@gmail.com', 'evseevagalina@rambler.ru',
          'sigizmund@hotmail.com', 'maslovepifan@hotmail.com', 'vikentivasilev@hotmail.com',
          'ermiltrofimov@hotmail.com', 'subbotinnikon@hotmail.com', 'polikarpshirjaev@yahoo.com', 'lukinjakov@mail.ru',
          'czatsev@yandex.ru', 'termakov@rambler.ru', 'valeri@yahoo.com', 'filimon@yandex.ru',
          'kkuznetsova@mail.ru']

for email in emails:
    domain = Domain.from_email(email)
    print(domain)

print("\n# TEST_6:")
urls = ['http://npo.com', 'http://zao.biz', 'http://ooo.edu', 'https://ooo.ru', 'http://prioskole.net',
        'http://ooo.com', 'http://bolshakova.biz', 'http://rao.biz', 'https://ip.biz', 'http://alekseev.ru',
        'http://ooo.ru', 'http://zao.biz', 'http://pk.biz', 'https://rao.biz', 'http://npo.org',
        'http://rao.com', 'http://rao.org', 'http://galkina.net', 'https://moskovskaja.biz', 'https://ao.ru']

for url in urls:
    domain = Domain.from_url(url)
    print(domain)

print("\n# TEST_7:")
domains = ['nikitin..biz', '.org', 'katren.', 'kubanskaja.edu.', '.', 'i.p.com', 'ooo.info+']

for d in domains:
    try:
        domain = Domain(d)
    except DomainException as e:
        print(e)

print("\n# TEST_8:")
emails = ['anan,i86@example.org', 'konovalovkondrat@@example.net', 'efimmaksimov@example..net', 'marfa_.04@example.com',
          'vlasovstanimir@example.org.', '.anikita_04@example.net', '@loginovroman@example.org', 'abc@@mail.ru',
          'novikovasinklitikija@example.net@', 'elizar_1978@example@.com', 'kasjan_1972@example.org', '@a.ru',
          'abc@.ru']

for email in emails:
    try:
        domain = Domain.from_email(email)
    except DomainException as e:
        print(e)

print("\n# TEST_9:")
urls = ['http://evseeva.info/', 'https:://ip.com/', 'https://www.ao.ru', 'https:///ip.ru', 'https://zao.',
        'https://.edu', 'http://oao.edu/', 'http://www.ip.com/', 'http://.org', 'http://abc.']

for url in urls:
    try:
        domain = Domain.from_url(url)
    except DomainException as e:
        print(e)

print("\n# TEST_10:")
domain1 = Domain('pygen.ru')  # непосредственно на основе домена
domain2 = Domain.from_url('https://pygen.ru')  # на основе url-адреса
domain3 = Domain.from_email('support@pygen.ru')  # на основе адреса электронной почты

print(type(domain1))
print(type(domain2))
print(type(domain3))
