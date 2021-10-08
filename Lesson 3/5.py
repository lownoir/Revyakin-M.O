# -- coding: utf-8 --
# По данному натуральному n вычислите сумму 1^3+2^3+3^3+...+n^3.

def sum_n():
    print('Введите n:')
    n = int(input())
    sum = 0

    for i in range(n+1):
        sum += (i ** 3)

    print(sum)
sum_n()