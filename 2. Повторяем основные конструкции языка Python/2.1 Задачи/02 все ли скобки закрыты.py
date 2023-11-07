# Назовем скобочной последовательностью строку, состоящую из символов ( и ). Будем считать скобочную последовательность
# правильной, если:
#
#     для каждой открывающей скобки есть закрывающая скобка
#     скобки закрываются в правильном порядке, то есть в каждой паре из открывающей и закрывающей скобок открывающая
#     находится левее
#
# Напишите программу, которая определяет, является ли скобочная последовательность правильной.
#
# Формат входных данных
# На вход программе подается строка, представляющая собой скобочную последовательность.
#
# Формат выходных данных
# Программа должна вывести True, если введенная скобочная последовательность является правильной,
# или False в противном случае.

string = input()
list_of_open_parentheses = []
answer = True
for parentheses in string:
    if not list_of_open_parentheses:
        if parentheses == '(':
            list_of_open_parentheses.append(parentheses)
        else:
            answer = False
            break
    else:
        if parentheses == list_of_open_parentheses[-1]:
            list_of_open_parentheses.append(parentheses)
        else:
            del list_of_open_parentheses[-1]
if list_of_open_parentheses:
    answer = False
print(answer)
