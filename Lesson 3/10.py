# -- coding: utf-8 --
# Пользователь вводит два числа N и K с клавиатуры. N - количество чисел из ряда Фибоначчи, K - порядковый номер в ряду, с которого нужно начать.

def sum_Fibonachi():
    N = int(input('Введите количество чисел: '))
    K = int(input('Введите порядковый номер: '))
    first = 0
    second = 1
    sum = 0
    if K < 3:
        sum += 1

    for i in range(2, N):
        num = first + second
        first, second = second, num
        
        if i >= (K-1):
            sum += num
    print(sum)
sum_Fibonachi()
        

