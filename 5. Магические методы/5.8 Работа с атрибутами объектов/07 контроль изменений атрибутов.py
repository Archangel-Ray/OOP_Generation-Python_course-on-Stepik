"""
Реализуйте класс Const. При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
    Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Класс Const должен разрешать устанавливать атрибуты своим экземплярам и получать их значения,
    но не разрешать изменять значения этих атрибутов, а также удалять их. При попытке изменить значение атрибута
    должно возбуждаться исключение AttributeError с текстом:

    Изменение значения атрибута невозможно

При попытке удалить атрибут должно возбуждаться исключение AttributeError с текстом:

    Удаление атрибута невозможно

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Const нет, она может быть произвольной.
"""


class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        else:
            self.__dict__[key] = value

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')


# INPUT DATA:

# TEST_1:
print("\nтест 1")
videogame = Const(name='Cuphead')

videogame.developer = 'Studio MDHR'
print(videogame.name)
print(videogame.developer)

# TEST_2:
print("\nтест 2")
videogame = Const(name='Dicso Elysium')

try:
    videogame.name = 'Half-Life: Alyx'
except AttributeError as e:
    print(e)

# TEST_3:
print("\nтест 3")
videogame = Const(name='The Last of Us')

try:
    del videogame.name
except AttributeError as e:
    print(e)

# TEST_4:
print("\nтест 4")
person = Const()

person.name = 'Erlich'
person.surname = 'Bachmann'

try:
    del person.name
except AttributeError as e:
    print(e)

try:
    person.surname = 'Hendrix'
except AttributeError as e:
    print(e)

# TEST_5:
print("\nтест 5")
work_obj = Const()

work = ['Designer, textile', 'Research scientist (physical sciences)', 'Heritage manager',
        'Civil engineer, contracting', 'Futures trader', 'Psychotherapist', 'Make',
        'English as a foreign language teacher', 'Publishing copy', 'Probation officer', 'Water quality scientist',
        'Magazine features editor', 'Designer, furniture', 'Merchant navy officer', 'Psychiatrist',
        'Biomedical engineer', 'Education officer, community', 'Paediatric nurse', 'Teacher, adult education',
        'Editor, magazine features', 'Scientist, research (medical)', 'Site engineer', 'Wellsite geologist',
        'Journalist, newspaper', 'Psychologist, prison and probation services', 'Therapist, drama', 'Data scientist',
        'Surveyor, hydrographic', 'Animal technologist', 'Brewing technologist', 'Materials engineer', 'Cabin crew',
        'Electronics engineer', 'Contractor', 'Mechanical engineer', 'Tree surgeon', 'Personal assistant',
        'Patent attorney', 'Librarian, academic', 'Haematologist', 'Conservator, furniture', 'Prison officer',
        'Designer, jewellery', 'Surgeon', 'Retail merchandiser', 'Producer, television/film/video', 'Dentist',
        'Primary school teacher', 'Engineer, mining', 'Theatre director', 'Chief of Staff', 'Forest/woodland manager',
        'Oncologist', 'Geoscientist', 'Clinical embryologist', 'Air cabin crew', 'Statistician', 'Administrator',
        'Occupational psychologist', 'General practice doctor', 'Psychotherapist, dance movement',
        'Environmental education officer', 'Librarian, public', 'Editorial assistant', 'Psychiatric nurse',
        'Colour technologist', 'Operational investment banker', 'Armed forces operational officer', 'Immunologist',
        'Arts administrator', 'Web designer', 'Maintenance engineer', 'Energy manager', 'Theme park manager',
        'Medical physicist', 'Lobbyist', 'Medical illustrator', 'Regulatory affairs officer',
        'Research scientist (maths)', 'Printmaker', 'Designer, industrial/product', 'Architectural technologist',
        'Field seismologist', 'Air traffic controller', 'Waste management officer', 'Firefighter',
        'Occupational therapist', 'Community arts worker', 'Commercial art gallery manager',
        'Public relations account executive', 'Historic buildings inspector/conservation officer',
        'Radiation protection practitioner', 'Editor, film/video', 'Database administrator', 'Youth worker',
        'Chemical engineer', 'Tour manager', 'Aid worker', 'Solicitor', 'Chiropodist']

work_obj.job = work[0]
for job in work[1:]:
    try:
        work_obj.job = job
    except AttributeError as e:
        print(e)
