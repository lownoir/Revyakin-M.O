# -*- coding: utf-8 -*-
# Шоколадка, дольки.

def choco():
    print("Введите размер шоколадки:")
    n = int(input())
    m = int(input())
    print("Введите из скольки долек должна состоять отломленная часть:")
    k = int(input())
    
    if k % n == 0:
        return 'Да'
    else:
        return 'Нет'
print(choco())