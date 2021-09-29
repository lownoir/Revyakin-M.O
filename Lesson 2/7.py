# -*- coding: utf-8 -*-
# Високосный год

def god():
    print("Введите год")
    y = int(input())
    if (y % 4 == 0) and (y % 100 > 0) or (y % 400 == 0):
        return 'Год високосный'
    else:
        return 'Год не високосный'

print (god())