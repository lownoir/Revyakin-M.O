# -- coding: utf-8 --
# По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N

def max_degree():
    N = int(input('Введите целое число:'))
    degree = 1
    while (2 ** (degree + 1)) <= N:
        degree += 1
    print(degree)
max_degree()