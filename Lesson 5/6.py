# -- coding: utf-8 --
# Определите среднее значение всех элементов последовательности, завершающейся числом 0

def average_value():
    S = 1
    print('Введите целые положительные числа: ')
    count = 0
    sum = 0
    while S != 0:
        S = int(input())
        count += 1
        sum += S
    print('Среднее значение последовательных чисел:', sum / count)
average_value()