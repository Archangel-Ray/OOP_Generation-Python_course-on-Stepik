"""
В этой задаче вам необходимо реализовать класс Testpaper, который позволит составлять экзаменационные тесты.
    Каждый тест должен создаваться на основе темы, схемы верных ответов и минимального процента верных решений:

    testpaper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
    testpaper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
    testpaper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

Созданные тесты должны сдаваться студентом — экземпляром класса Student. Он должен иметь метод take_test(), который
    принимает в качестве аргументов тест и ответы студента на этот тест:

    student1 = Student()
    student2 = Student()

    student1.take_test(testpaper1, ['1A', '2D', '3D', '4A', '5A'])
    student2.take_test(testpaper2, ['1C', '2D', '3A', '4C'])
    student2.take_test(testpaper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])

Результаты тестов должны быть доступны в виде словаря, ключом в котором является тема теста,
    а значением — результат теста (сдан или не сдан) и процент верных решений:

    print(student1.tests_taken)    # {'Maths': 'Passed! (80%)'}
    print(student2.tests_taken)    # {'Chemistry': 'Failed! (25%)', 'Computing': 'Failed! (43%)'}

Если студент еще не сдал ни одного теста, атрибут tests_taken должен содержать строку No tests taken:

    student3 = Student()

    print(student3.tests_taken)    # No tests taken

Примечание 1. Округление процента верных решений должно происходить до ближайшего целого числа.
"""


class Testpaper:
    def __init__(self, topic, answers, percentage):
        self.topic = topic
        self.answers = answers
        self.percentage = percentage


class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"

    def take_test(self, testpaper, answers):
        if type(self.tests_taken) is str:
            self.tests_taken = {}
        correctness = [x[0] == x[1] for x in zip(testpaper.answers, answers)]
        grade_for_a_test = round(sum(correctness) / (len(correctness) / 100))
        self.tests_taken[testpaper.topic] = f"{'Passed!' if grade_for_a_test > 50 else 'Failed!'} ({grade_for_a_test}%)"


# INPUT DATA:

print("\n# TEST_1:")
paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

student1 = Student()
student2 = Student()

student1.take_test(paper1, ['1A', '2D', '3D', '4A', '5A'])
student2.take_test(paper2, ['1C', '2D', '3A', '4C'])
student2.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])

print(student1.tests_taken)
print(student2.tests_taken)

print("\n# TEST_2:")
paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

student = Student()

print(student.tests_taken)

print("\n# TEST_3:")
papers = [
    Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%'),
    Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%'),
    Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%'),
    Testpaper(
        'Informatics',
        ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8A', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
         '18B', '19D', '20D'],
        '90%'
    )
]

student1 = Student()
student2 = Student()

student1.choices = [
    ['1C', '2B', '3D', '4C', '5B'],
    ['1A', '2D', '3A', '4D'],
    ['1B', '2D', '3D', '4C', '5B', '6C', '7C'],
    ['1B', '2A', '3C', '4C', '5A', '6B', '7C', '8B', '9D', '10C', '11A', '12D', '13C', '14A', '15B', '16A', '17C',
     '18B', '19C', '20B']
]

student2.choices = [
    ['1A', '2A', '3A', '4A', '5C'],
    ['1A', '2C', '3C', '4A'],
    ['1A', '2B', '3C', '4A', '5D', '6D', '7D'],
    ['1B', '2A', '3C', '4C', '5A', '6D', '7C', '8D', '9A', '10B', '11D', '12A', '13B', '14B', '15C', '16D', '17A',
     '18A', '19D', '20C']
]

for student in [student1, student2]:
    for i in range(4):
        student.take_test(papers[i], student.choices[i])
print(student1.tests_taken)
print(student2.tests_taken)

print("\n# TEST_4:")
papers = [
    Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%'),
    Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%'),
    Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%'),
    Testpaper(
        'Informatics',
        ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8A', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
         '18B', '19D', '20D'],
        '90%'
    )
]

student = Student()

student.choices = [
    ['1A', '2C', '3D', '4B', '5A'],
    ['1C', '2A', '3D', '4A'],
    ['1D', '2C', '3C', '4B', '5D', '6A', '7A'],
    ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8B', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
     '18B', '19D', '20D']
]

for i in range(4):
    student.take_test(papers[i], student.choices[i])

print(student.tests_taken)
