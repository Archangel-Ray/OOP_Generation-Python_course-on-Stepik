"""
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Gun должен иметь три метода экземпляра:

    shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf,
    при третьем — pif, при четвертом — paf, и так далее
    shots_count() — метод, возвращающий актуальное количество вызовов метода shoot()
    shots_reset() — метод, сбрасывающий количество вызовов метода shoot() до нуля
"""


class Gun:
    def __init__(self):
        self.number_of_shots = 0

    def next_shoot(self):
        self.number_of_shots += 1

    def shoot(self):
        if self.number_of_shots % 2 == 0:
            print('pif')
            self.next_shoot()
        else:
            print('paf')
            self.next_shoot()

    def shots_count(self):
        return self.number_of_shots

    def shots_reset(self):
        self.number_of_shots = 0


gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
