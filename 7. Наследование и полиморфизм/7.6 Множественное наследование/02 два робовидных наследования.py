"""
С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов
"""


class H:
    pass


class D(H):
    pass


class E(H):
    pass


class F(H):
    pass


class G(H):
    pass


class B(D, E):
    pass


class C(F, G):
    pass


class A(B, C):
    pass


# INPUT DATA:

print("\n# TEST_1:")
print(issubclass(D, H))
print(issubclass(E, H))
print(issubclass(F, H))
print(issubclass(G, H))

print("\n# TEST_2:")
print(issubclass(B, D))
print(issubclass(B, E))
print(issubclass(B, F))
print(issubclass(B, G))

print("\n# TEST_3:")
print(issubclass(C, D))
print(issubclass(C, E))
print(issubclass(C, F))
print(issubclass(C, G))

print("\n# TEST_4:")
print(A.mro())

print("\n# TEST_5:")
print(issubclass(A, H))
print(issubclass(B, H))
print(issubclass(C, H))
