"""
Реализуйте класс Тodo, описывающий список дел. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса Тodo должен иметь один атрибут:

    things — изначально пустой список дел, которые нужно выполнить

Класс Тodo должен иметь четыре метода экземпляра:

    add() — метод, принимающий название дела и его приоритет (целое число) и
    добавляющий данное дело в список дел в виде кортежа:

    (<название дела>, <приоритет>)

    get_by_priority() — метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел,
    имеющих приоритет n
    get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет
    get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет

Примечание 1. Названия дел в списках, возвращаемых методами get_by_priority(), get_low_priority() и get_high_priority(),
должны располагаться в том порядке, в котором они были добавлены в список.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
"""


class Todo:
    def __init__(self):
        self.things = list()

    def add(self, case_name, priority):
        self.things.append((case_name, priority))

    def get_by_priority(self, n):
        return [name for name, prior in self.things if prior == n]

    def get_low_priority(self):
        min_prior = min([x[1] for x in self.things]) if self.things else None
        return self.get_by_priority(min_prior)

    def get_high_priority(self):
        max_prior = max([x[1] for x in self.things]) if self.things else None
        return self.get_by_priority(max_prior)


# INPUT DATA:

# TEST_1:
todo = Todo()

print(todo.things)
print(todo.get_by_priority(1))
print(todo.get_low_priority())
print(todo.get_high_priority())

# TEST_2:
todo = Todo()

todo.add('Проснуться', 3)
todo.add('Помыться', 2)
todo.add('Поесть', 2)

print(todo.get_by_priority(2))

# TEST_3:
todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))

# TEST_4:
todo = Todo()

todos = [
    'Выбрать хостинг для своего сайта',
    'Записаться к стоматологу',
    'Записаться на курсы английского',
    'Навести порядок на кухне',
    'Подготовить одежду к лету',
    'Подготовиться к выступлению в понедельник',
    'Помыть машину',
    'Пропылесосить ковры',
    'Свозить Кемаля к ветеринару',
    'Сходить в парикмахерскую',
    'Посетить выставку камней'
]

priorities = [4, 1, 2, 5, 2, 5, 5, 3, 3, 3, 4]
for t, p in zip(todos, priorities):
    todo.add(t, p)

print(todo.get_by_priority(3))
print(todo.get_low_priority())
print(todo.get_high_priority())
