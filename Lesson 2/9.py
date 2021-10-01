# -*- coding: utf-8 -*-
# Шоколадка, дольки.

def choco():
    print("Введите размер шоколадки:")
    n = int(input())
    m = int(input())
    print("Введите из скольки долек должна состоять отломленная часть:")
    k = int(input())
    
    if (k < n*k) and ((k % n == 0) or (k % m == 0)):
        return 'Да'
    else:
        return 'Нет'
print(choco())
