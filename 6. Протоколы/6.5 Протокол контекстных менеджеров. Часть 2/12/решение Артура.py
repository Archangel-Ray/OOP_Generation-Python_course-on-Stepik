class TreeBuilder:
    def __init__(self):
        self.knots = [[]]

    def __enter__(self):
        self.knots.append([])

    def __exit__(self, *args, **kwargs):
        if self.knots[-1]:
            self.knots[-2].append(self.knots[-1])
        self.knots.pop()

    def add(self, value):
        self.knots[-1].append(value)

    def structure(self):
        return self.knots[-1]


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
