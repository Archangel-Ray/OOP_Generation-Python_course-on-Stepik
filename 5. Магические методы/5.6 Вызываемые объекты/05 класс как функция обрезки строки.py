"""
Реализуйте класс Strip, экземпляры которого позволяют удалять из начала и конца строки определенные символы.
При создании экземпляра класс должен принимать один аргумент:

    chars — строка, в которой перечислены удаляемые символы

Экземпляр класса Strip должен являться вызываемым объектом и принимать один аргумент:

    string — строка

Экземпляр класса Strip должен удалять из начала и конца строки string все символы,
перечисленные в chars, и возвращать полученный результат.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Strip нет, она может быть произвольной.
"""


class Strip:
    def __init__(self, chars_):
        self.chars = chars_

    def __call__(self, string):
        start_of_line = 0
        while string[start_of_line] in self.chars:
            start_of_line += 1
        end_of_line = -1
        while string[end_of_line] in self.chars:
            end_of_line -= 1

        return string[start_of_line:end_of_line + 1] if end_of_line < -1 else string[start_of_line:]


# INPUT DATA:

# TEST_1:
print('\nтест 1')
strip = Strip('!? ')

print(strip('     ?beegeek!'))
print(strip('!bee?geek!'))

# TEST_2:
print('\nтест 2')
strip = Strip('.,+-')

print(strip('     --++beegeek++--'))
print(strip('-bee...geek-'))
print(strip('-+,.b-e-e-g-e-e-k-+,.'))

# TEST_3:
print('\nтест 3')
chars_sequence = ["X'r", 'q8|', 'M8y', 'uE^', 'N9F', '"kw', '5j_', '" t', 'klB', 'a=']
words = ["XrragainX'X", '8||bring||8', 'yyyfamily8y8', '^^^put^^u', '99Feight9FF', '"k"protectwwk', 'jjjoptionj55',
         't" responsettt', 'kkBrisekBB', 'a=anationala==']

for word in words:
    for chars in chars_sequence:
        strip = Strip(chars)
        word = strip(word)
    print(word)

# TEST_4:
print('\nтест 4')
from string import punctuation

strip = Strip(punctuation)
words = ['&}:,"@team-..|][', '[${!."language+>}*{@', ')..?(?throughout/?`%%^', '%](+{!dog\\_];]:', "+]@@'?wide[={[&_",
         "<%:#<_director!']>?$", '&__$>.onto#;|~$-', '@,}]).of?/)?=!', '<%@^:}company\'!#("^', '?@.[^|run#<\\~\\[',
         "<|%;#=father<:;@'=", ')\\`-&)street+)(#\\~', '((%/?$enough~\\<{${', '*@;{.@young!(_.:)', '?<;<}&health#!=[~^',
         ".&]+'/learn)-@@)+", "@$,,]/entire;)$'@>", '*"%=+?use#!?#``', '&:|%_+first:@+{}+', '`<&=@.heavy{(}^\\-',
         ":,]'.=argue&(([|/", '*\\|^!|mother_\\$,]_', '\'>\'@|@owner";\\)}.', '~+=+=%new?]]_!.', '<&{+$@check|\\;[*[',
         '([*;;^explain%(~"]^', ')|,){+late.,"%,(', '|~\\-{:movie.,~/}\\', ')%*=}?card<{^`>|', '$!,<+)raise+,<{<%',
         '#?:=!}direction>`\'"#*', '!/|)()article_/]),,', ']\'"=.-trouble#%\\*%$', "}^={=\\happen!)]':^",
         '`://..move)),%-&', '*`=;>.anyone&-`</,', "}^`{%'near@.+,{&", '%/<*;>short-&{*<-', '^&&(^!really=;?{`"',
         '^,=}!=check\\{*-!`', '_=?[*`management/(:)?,', '![]_]/boy$-@`&:', '.):\\,}or?]$?;*', '\\^.{:@very=@!!]=',
         '*\\@~+=attack~=>+.)', '%"`/.:available}*<~)@', "*,-\\'~sell-?;>!\\", ',)^["[executive::;_[:',
         '&#:":*up~.{`|$', '+}@_=>floor-`}`~@']

for word in words:
    print(strip(word))
