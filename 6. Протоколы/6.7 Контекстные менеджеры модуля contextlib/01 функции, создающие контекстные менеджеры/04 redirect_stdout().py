from contextlib import redirect_stdout
"""
используется для построения контекстных менеджеров, которые временно перенаправляют поток sys.stdout 
    в указанный файлоподобный объект.
"""

# создает файл output.txt:
with open('output.txt', mode='w', encoding='utf-8') as file:
    with redirect_stdout(file):
        print('Python generation!')
        help(len)
