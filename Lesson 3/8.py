# -- coding: utf-8 --
# По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.

def stairs():
    print('Введите число <= 9:')
    n = int(input())
    stair = 1
    if (1 < n <= 9):
        print(stair)
        for i in range(2, n+1):
            stair =str(stair) + str(i)
            print(stair)
    else:
        print('Число больше 9!')
stairs()
