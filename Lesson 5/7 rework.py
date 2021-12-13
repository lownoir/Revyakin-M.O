# -- coding: utf-8 --

def count_more():
    a=1
    b = 0
    S = int(input("Введите число: "))
    e = S
    while True:
        S = int(input())
        if S == 0:
            break
        if a!=0:
            if S > e :
                b += 1
            else:
                a=0
        e = S
    print(b)
count_more()