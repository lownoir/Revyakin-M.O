# -- coding: utf-8 --

def count_prev():
    print('Введите целые положительные числа: ')
    prev_number = int(input())
    count = 0
    S = 1
    while S != 0:
        S = int(input())
        if S > prev_number:
            count += 1
        prev_number = S
    print('Количество чисел:', count)
count_prev()