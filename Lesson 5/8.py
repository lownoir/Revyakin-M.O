# -- coding: utf-8 --
# Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

def max_elements():
    print('Введите целые положительные числа:')
    prev_num = int(input())
    max_1 = 1
    max_2 = 1
    S = 1
    while S != 0:
        S = int(input())
        if prev_num == S:
            max_1 += 1
            if max_1 > max_2:
                max_2 = max_1
        else:
            max_1 = 1
        prev_num = S
    print('Наибольшее число:', max_2)
max_elements()