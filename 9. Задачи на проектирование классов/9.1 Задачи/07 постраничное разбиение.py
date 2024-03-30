"""
Реализуйте класс Pagination для обработки данных с разбивкой по страницам. Разбивка по страницам используется
    для разделения большого количества данных на части. Экземпляр класса Pagination должен создаваться
    на основе двух значений:

    исходные данные, представленные в виде списка с произвольными элементами
    размер страницы, то есть количество элементов, отображаемых на каждой странице

alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)

Для получения содержимого страницы должен использоваться метод get_visible_items():

print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

Обратите внимание, содержимое страницы должно быть представлено в виде списка. Перемещение по страницам должно
    происходить с помощью следующих методов:

    prev_page() — вернуться к предыдущей странице
    next_page() — перейти к следующей странице
    first_page() — вернуться к первой странице
    last_page() — перейти к последней странице
    go_to_page() — перейти к странице с указанным номером (1 — первая страница, 2 — вторая страница, и так далее)

pagination.next_page()
print(pagination.get_visible_items())    # ['e', 'f', 'g', 'h']

pagination.last_page()
print(pagination.get_visible_items())    # ['y', 'z']

Методы для перемещения по страницам должны быть применимы друг за другом:

pagination.first_page()
pagination.next_page().next_page()
print(pagination.get_visible_items())    # ['i', 'j', 'k', 'l']

С помощью атрибутов total_pages и current_page должна быть возможность получить общее количество страниц
    и текущую страницу соответственно:

    print(pagination.total_pages)            # 7
    print(pagination.current_page)           # 3

При нахождении на первой странице и перемещении к предыдущей странице, текущей страницей должна остаться
    первая страница. Аналогично при нахождении на последней странице и перемещении к следующей странице,
    текущей страницей должна остаться последняя страница:

    pagination.first_page()
    pagination.prev_page()
    print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

    pagination.last_page()
    pagination.next_page()
    print(pagination.get_visible_items())    # ['y', 'z']

При перемещении к нулевой или менее странице, текущей страницей должна стать первая страница.
    Аналогично при перемещении к странице, номер которой превышает общее количество страниц,
    текущей страницей должна стать последняя страница:

    pagination.go_to_page(-100)
    print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

    pagination.go_to_page(100)
    print(pagination.get_visible_items())    # ['y', 'z']
"""


class Pagination:
    def __init__(self, list_obj, len_list):
        self.list_pages = []
        while list_obj:
            self.list_pages.append(list_obj[:len_list])
            list_obj = list_obj[len_list:]
        self.current_page = 1

    def get_visible_items(self):
        return self.list_pages[self.current_page - 1]

    def go_to_page(self, page):
        if page < 0:
            self.first_page()
        elif page >= len(self.list_pages):
            self.last_page()
        elif 0 <= page < len(self.list_pages):
            self.current_page = page

    def prev_page(self):
        if self.current_page - 1 > 0:
            self.current_page -= 1
        return self

    def next_page(self):
        if self.current_page + 1 < len(self.list_pages) + 1:
            self.current_page += 1
        return self

    def first_page(self):
        self.current_page = 1

    def last_page(self):
        self.current_page = len(self.list_pages)

    @property
    def total_pages(self):
        return len(self.list_pages)


# INPUT DATA:

print("\n# TEST_1:")
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
print(pagination.get_visible_items())

print("\n# TEST_2:")
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
pagination.next_page()
print(pagination.get_visible_items())

pagination.last_page()
print(pagination.get_visible_items())

print("\n# TEST_3:")
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
pagination.next_page().next_page()
print(pagination.get_visible_items())
print(pagination.total_pages)
print(pagination.current_page)

print("\n# TEST_4:")
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
pagination.prev_page()
print(pagination.get_visible_items())

pagination.last_page()
pagination.next_page()
print(pagination.get_visible_items())

print("\n# TEST_5:")
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
pagination.go_to_page(-100)
print(pagination.get_visible_items())

pagination.go_to_page(100)
print(pagination.get_visible_items())

print("\n# TEST_6:")
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)
print(pagination.get_visible_items())

print("\n# TEST_7:")
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)
pagination.next_page()
print(pagination.get_visible_items())

pagination.last_page()
print(pagination.get_visible_items())

pagination.first_page()
print(pagination.get_visible_items())

print("\n# TEST_8:")
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)
pagination.next_page().next_page()
print(pagination.get_visible_items())
print(pagination.total_pages)
print(pagination.current_page)

print("\n# TEST_9:")
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)
pagination.prev_page()
print(pagination.get_visible_items())

pagination.last_page()
pagination.next_page()
print(pagination.get_visible_items())

print("\n# TEST_10:")
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)
pagination.go_to_page(-100)
print(pagination.get_visible_items())

pagination.go_to_page(100)
print(pagination.get_visible_items())

print("\n# TEST_11:")
text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кощей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.'''.splitlines()

pagination = Pagination(text, 5)

pagination.last_page()
pagination.prev_page().prev_page()
print(pagination.get_visible_items())

print("\n# TEST_12:")
alphabet = list('abcd')

pagination = Pagination(alphabet, 4)
pagination.next_page()
print(pagination.get_visible_items())

print("\n# TEST_13:")
alphabet = list('abcdefghijklmnopqrstuvwxyz')
pagination = Pagination(alphabet, 4)
pages = [7, 3, 6, 1, 4, 2, 5]

for page_ in pages:
    pagination.go_to_page(page_)
    print(pagination.get_visible_items())
