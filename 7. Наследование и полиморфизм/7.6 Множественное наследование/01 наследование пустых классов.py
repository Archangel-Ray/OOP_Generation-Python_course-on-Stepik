"""
С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов
"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


class E(B, D):
    pass


# INPUT DATA:

print("\n# TEST_1:")
print(issubclass(E, B))
print(issubclass(E, C))
print(issubclass(E, D))

print("\n# TEST_2:")
print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(D, A))

print("\n# TEST_3:")
print(E.mro())

print("\n# TEST_4:")
print(issubclass(E, A))
