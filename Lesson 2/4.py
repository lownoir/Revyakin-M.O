# -*- coding: utf-8 -*-
# Длина шнурка
def func():
    print("Введите расстояние между рядами:")
    a = int(input())
    print("Введите расстояние между дырочками:")
    b = int(input())
    print("Введите длину свободного конца шнурка:")
    l = int(input())
    print("Введите кол-во дырочек в каждом ряду:")
    N = int(input())
    print("Длина:")
    return (N*b-b+l) + (N*a-a)

print(func())
