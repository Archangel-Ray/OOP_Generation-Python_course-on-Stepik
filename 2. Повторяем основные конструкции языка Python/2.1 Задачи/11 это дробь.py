# удем считать обыкновенной дробью последовательность из одной или более цифр, за которой следует прямая косая черта /,
# а затем — последовательность из одной или более цифр, хотя бы одна из которых отлична
# от нуля (знаменатель не может равняться нулю). Последовательность, представляющая собой обыкновенную дробь,
# может начинаться с необязательного символа дефиса -.
#
# Реализуйте функцию is_fraction(), которая принимает один аргумент:
#
#     string — строка, содержащая произвольный набор символов
#
# Функция должна возвращать True, если строка string представляет собой обыкновенную дробь,
# или False в противном случае.


def is_fraction(string):
    if string:
        if string[0] == '-':
            string = string[1:]
    else:
        return False

    if '/' in string:
        string = string.split('/')
        if len(string) == 2:
            if string[0].isdigit():
                if string[1].isdigit():
                    if int(string[1]) > 0:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


# INPUT DATA:

# TEST_1:
print(is_fraction('1000/1'))

# TEST_2:
print(is_fraction('-54/9'))

# TEST_3:
print(is_fraction('71'))

# TEST_4:
print(is_fraction('1 / 82'))

# TEST_5:
print(is_fraction('1/0'))

# TEST_6:
print(is_fraction(''))

# TEST_7:
print(is_fraction('/4'))

# TEST_8:
print(is_fraction('1000'))

# TEST_9:
print(is_fraction('-987/1'))

# TEST_10:
print(is_fraction('0/1'))

# TEST_11:
print(is_fraction('-/56'))

# TEST_12:
print(is_fraction('1/1234'))

# TEST_13:
print(is_fraction('2-/4'))

# TEST_14:
print(is_fraction('3/-7'))

# TEST_15:
print(is_fraction('5/8-'))

# TEST_16:
print(is_fraction('--1/2'))

# TEST_17:
print(is_fraction('-7/3-'))

# TEST_18:
print(is_fraction('-7-/-3-'))

# TEST_19:
print(is_fraction('/4/5'))

# TEST_20:
print(is_fraction('4/5/'))

# TEST_21:
print(is_fraction('54365486548645/472342935648904709456'))

# TEST_22:
print(is_fraction('5/2/4'))

# TEST_23:
print(is_fraction('5/2/4/2'))

# TEST_24:
print(is_fraction('1000/10'))

# TEST_25:
print(is_fraction('1000/00001'))
print(is_fraction('-1000/00001'))

# TEST_26:
print(is_fraction('1000/00004123'))
print(is_fraction('1000/0000'))
print(is_fraction('1000/00000008000'))
