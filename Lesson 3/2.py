# -- coding: utf-8 --
# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.

def output():
    print('Введите 2 целых числа (A, B):')
    A = int(input())
    B = int(input())

    if A < B:
        for i in range(A, B+1):
            print(i)
    else:
        for i in range(A, B-1, -1):
            print(i)
output()