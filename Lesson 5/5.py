# -- coding: utf-8 --
# Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке.

def numbers():
    S = 1
    count = 0
    print('Введите целые положительные числа: ')
    while S != 0:
        S = int(input())
        count += 1
    print('Количество членов последовательности:',count - 1)
numbers()