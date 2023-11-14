"""
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Gun должен иметь один метод экземпляра:

    shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif,
    при четвертом — paf, и так далее
"""


class Gun:
    def __init__(self):
        self.next = True

    def shoot(self):
        if self.next:
            print('pif')
            self.next = False
        else:
            print('paf')
            self.next = True


gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
