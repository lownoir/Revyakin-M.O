# -*- coding: utf-8 -*-
# Напишите функцию, которая вычисляет наименьшее из трех чисел и выводит на экран.

def func():
    print("Введите 3 числа:")
    a = int(input())
    b = int(input())
    c = int(input())
    print("Наименьшее:")
    return min(a,b,c)

print (func())
