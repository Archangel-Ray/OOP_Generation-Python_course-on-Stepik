# Реализуйте пустой класс PiggyBank, а затем создайте два экземпляра этого класса и
# присвойте их переменным money_box1 и money_box2.
#
# Экземпляр money_box1 должен иметь:
#
#     атрибут coins со значением 10
#
# Экземпляр money_box2 должен иметь:
#
#     атрибут coins со значением 15
#     атрибут color со значением 'pink'


class PiggyBank:
    pass


money_box1 = PiggyBank()
money_box1.coins = 10
money_box2 = PiggyBank()
money_box2.coins = 15
money_box2.color = 'pink'
print(PiggyBank.__dict__)
print(money_box1.__dict__)
print(money_box2.__dict__)
