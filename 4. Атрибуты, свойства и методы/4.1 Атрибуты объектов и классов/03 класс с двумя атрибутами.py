# Реализуйте класс PiggyBank, а затем создайте экземпляр этого класса и присвойте его переменной money_box.
#
# Класс PiggyBank должен иметь:
#
#     атрибут content со значением 'coins'
#     атрибут alternate_name со значением 'penny bank'


class PiggyBank:
    content = 'coins'
    alternate_name = 'penny bank'


money_box = PiggyBank()
print(money_box.__dir__())
