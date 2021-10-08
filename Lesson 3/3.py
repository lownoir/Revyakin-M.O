# -- coding: utf-8 --
# Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания.

def uneven():
    A = 13
    B = 5

    if A % 2 == 0:
        for i in range(A-1, B-1, -2):
            print(i)
    else:
        for i in range(A, B, -2):
            print(i)
uneven()