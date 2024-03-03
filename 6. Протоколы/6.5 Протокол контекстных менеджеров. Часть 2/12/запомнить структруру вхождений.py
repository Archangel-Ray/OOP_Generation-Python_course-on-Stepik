"""
недоделал...
слишком много времени ушло на это задание, надо продвигаться вперёд. вернусь сюда позже, если вспомню.
-----------------------------------------------------------------------------------------------------
Дерево — одна из наиболее широко распространённых структур данных в информатике,
    эмулирующая древовидную структуру в виде набора связанных узлов.

Элементы дерева называются узлами. На рисунке выше узлами являются значения 8, 3, 1, 6, 4, 7, 10, 14 и 13.
    Узлы без потомков называются листьями. На рисунке выше листьями являются значения 1, 4, 7 и 13.

Реализуйте класс TreeBuilder. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса TreeBuilder должен являться реентерабельным контекстным менеджером, который позволяет пошагово
    строить древовидную структуру данных (дерево).

Класс TreeBuilder должен иметь два метода экземпляра:

    add() — метод, принимающий в качестве аргумента произвольный объект (лист) и добавляющий его в текущий узел дерева
    structure() — метод, возвращающий структуру дерева в виде вложенных списков

Добавление узлов в дерево должно происходить с помощью оператора with. Узел считается текущим в рамках своего
    блока with. Если в узел не было добавлено ни одного листа, то этот узел не должен появляться в структуре дерева,
    возвращаемой методом structure().

Примечание 1. Структура дерева может быть произвольной, то есть узел может содержать другой узел,
                тот, в свою очередь, другой, и так далее.

Примечание 2. Гарантируется, что структура дерева не выводится внутри блоков with, то есть структура дерева
                выводится лишь после ее построения.

Примечание 3. Наглядные примеры использования класса TreeBuilder продемонстрированы в тестовых данных.

Примечание 4. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 5. Класс TreeBuilder должен удовлетворять протоколу контекстного менеджера,
                то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.
"""


class TreeBuilder:
    def __init__(self):
        self.tree = list()
        self.current_list = list()
        self.tree.append(self.current_list)
        self.level = 1

    def __enter__(self):
        self.new_list = list()
        self.current_list.append(self.new_list)
        self.current_list = self.new_list
        self.level += 1
        return self.current_list

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
        if not self.current_list:
            self.tree[-1][-1].pop()
        if self.level:
            self.current_list = self.tree[-1][-1]
        else:
            self.current_list = self.tree

    def add(self, obj):
        self.current_list.append(obj)

    def structure(self):
        return self.tree[0]


# INPUT DATA:

# TEST_1:
print('\nтест 1')
tree = TreeBuilder()
print(tree.structure(), [] == tree.structure())

tree.add('1st')
print(tree.structure(), ['1st'] == tree.structure())

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
    tree.add('4th')
    with tree:
        pass

print(tree.structure(), ['1st', ['2nd', ['3rd'], '4th']] == tree.structure())

# TEST_2:
print('\nтест 2')
tree = TreeBuilder()

tree.add('1st')

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
        with tree:
            tree.add('4th')
            with tree:
                tree.add('5th')
    with tree:
        pass

tree.add('6th')
print(tree.structure(), ['1st', ['2nd', ['3rd', ['4th', ['5th']]]], '6th'] == tree.structure())

# TEST_3:
print('\nтест 3')
tree = TreeBuilder()

with tree:
    tree.add(1)
    tree.add(2)
    with tree:
        tree.add(3)
        with tree:
            tree.add(4)
    with tree:
        tree.add(5)

print(tree.structure(), [[1, 2, [3, [4]], [5]]] == tree.structure())

# TEST_4:
print('\nтест 4')
tree = TreeBuilder()

with tree:
    tree.add(1)
    with tree:
        tree.add(2)
        tree.add(3)
    with tree:
        pass

print(tree.structure(), [[1, [2, 3]]] == tree.structure())

# TEST_5:
print('\nтест 5')
tree = TreeBuilder()

tree.add(0)
print(tree.structure(), [0] == tree.structure())

with tree:
    tree.add(1)
    with tree:
        tree.add(2)
        tree.add(3)
        with tree:
            tree.add(4)
    with tree:
        pass

print(tree.structure(), [0, [1, [2, 3, [4]]]] == tree.structure())

with tree:
    tree.add(5)
    with tree:
        tree.add(6)
    with tree:
        tree.add(7)
        with tree:
            tree.add(8)

print(tree.structure(), [0, [1, [2, 3, [4]]], [5, [6], [7, [8]]]] == tree.structure())

# TEST_6:
print('\nтест 6')
tree = TreeBuilder()

tree.add('root')
with tree:
    tree.add('first child')
    tree.add('second child')
    with tree:
        tree.add('grandchild')
    tree.add('bastard')
    with tree:
        pass
    tree.add('another bastard')

print(tree.structure(),
      ['root', ['first child', 'second child', ['grandchild'], 'bastard', 'another bastard']] == tree.structure())

# TEST_7:
print('\nтест 7')
tree = TreeBuilder()

tree.add('1st')

with tree:
    with tree:
        with tree:
            with tree:
                tree.add('5th')

print(tree.structure(), ['1st', [[[['5th']]]]] == tree.structure())

# TEST_8:
print('\nтест 8')
tree1 = TreeBuilder()
tree2 = TreeBuilder()

tree1.add('1st')

with tree1:
    tree1.add('2nd')
    with tree1:
        tree1.add('3rd')
    tree1.add('4th')
    with tree1:
        pass

print(tree1.structure(), ['1st', ['2nd', ['3rd'], '4th']] == tree1.structure())
print(tree2.structure(), [] == tree2.structure())
