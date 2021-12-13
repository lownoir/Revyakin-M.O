# -- coding: utf-8 --

def uneven():
    K = int(input())
    N = int(input())
    s = 0
    a = b = 1
    c = 2
    for i in range(2, K + N):
        if i >= K :s += c
        c = a + b
        a = b
        b = c
    print(s)
uneven()