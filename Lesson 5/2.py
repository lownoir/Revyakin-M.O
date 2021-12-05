# -- coding: utf-8 --
# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

def smallest():
    N = int(input('Введите число, не меньшее 2: '))
    div = 2
    while (N % div) > 0:
        div += 1
    print(div)
smallest()