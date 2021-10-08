# -- coding: utf-8 --
# Пользователь вводит число N с клавиатуры - количество чисел из ряда Фибоначчи. Посчитайте сумму этих чисел.

def sum_fibonachi():
    N = int(input('Введите количество чисел: '))
    first = 0
    second = 1
    sum = 1
    number = 0

    for i in range(2, N+1):
        sum += number
        number = first + second
        first, second = second, number
    print(sum)
sum_fibonachi()
