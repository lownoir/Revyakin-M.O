# -- coding: utf-8 --
# Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.

def f_count():

    S = str(input('Введите строку: '))
    count_l = S.count('f')
    if count_l >= 2:
        print(S.find('f'), S.rfind('f'))
    if count_l == 1:
        print(S.find('f'))
    else:
        None

f_count()