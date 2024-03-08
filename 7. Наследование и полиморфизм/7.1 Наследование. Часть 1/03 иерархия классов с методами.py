"""
С помощью наследования и приведенной ниже схемы постройте иерархию классов, описывающих животных:

Класс Animal должен иметь два метода экземпляра:

    sleep() — пустой метод
    eat()— пустой метод

Класс Fish должен иметь один метод экземпляра:

    swim()— пустой метод

Класс Bird должен иметь один метод экземпляра:

    lay_eggs()— пустой метод

Класс FlyingBird должен иметь один метод экземпляра:

    fly()— пустой метод
"""


class Animal:
    def sleep(self):
        pass

    def eat(self):
        pass


class Fish(Animal):
    def swim(self):
        pass


class Bird(Animal):
    def lay_eggs(self):
        pass


class FlyingBird(Bird):
    def fly(self):
        pass


# INPUT DATA:

# TEST_1:
print("\nтест 1")
print(issubclass(Fish, Animal))
print(issubclass(Bird, Animal))
print(issubclass(FlyingBird, Animal))
print(issubclass(FlyingBird, Bird))

# TEST_2:
print("\nтест 2")
animal = Animal()

print(animal.sleep())
print(animal.eat())

# TEST_3:
print("\nтест 3")
fish = Fish()

print(fish.sleep())
print(fish.eat())
print(fish.swim())

# TEST_4:
print("\nтест 4")
bird = Bird()
print(bird.sleep())
print(bird.eat())
print(bird.lay_eggs())

# TEST_5:
print("\nтест 5")
flying_bird = FlyingBird()
print(flying_bird.sleep())
print(flying_bird.eat())
print(flying_bird.lay_eggs())
print(flying_bird.fly())

# TEST_6:
print("\nтест 6")
animal = Animal()

methods = ['swim', 'lay_eggs', 'fly']
for method in methods:
    print(hasattr(animal, method))
