# -- coding: utf-8 --

from tkinter import*
from tkinter import font
window = Tk()
window.title('Python GUI for Lesson 6')
window.geometry('1800x800')

def sqrt():
    a = txt_1.get()
    N = int(a)
    s = 1
    res = ''
    while s ** 2 <= N:
        res += str(s ** 2)
        s += 1
        res = res + ' '
    answer_1.configure(text = res)

tsk1 = Label(window, text='1) По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.', font=("Arial", 11, 'bold'))
tsk1.place(x=10, y=20)
t1 = Label(window, text='Введите N:')
t1.place(x=10, y=50)
txt_1 = Entry(window, width=10)
txt_1.place(x=80, y=50)
btn1 = Button(window, text='Решить', command=sqrt)
btn1.place(x=150, y=46)
otvet1 = Label(window, text='Ответ: ')
otvet1.place(x=205, y=50)
answer_1 = Label(window, text='', font=('Arial', 10, 'bold'))
answer_1.place(x=245, y=50)

def smallest():
    a = txt_2.get()
    N = int(a)
    div = 2
    while (N % div) > 0:
        div += 1
    answer_2.configure(text = div)

tsk2 = Label(window, text='2) Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.', font=("Arial", 11, 'bold'))
tsk2.place(x=10, y=75)
t2 = Label(window, text='Введите число:')
t2.place(x=10, y=105)
txt_2 = Entry(window, width=10)
txt_2.place(x=100, y=105)
btn2 = Button(window, text='Решить', command=smallest)
btn2.place(x=170, y=101)
otvet2 = Label(window, text='Ответ: ')
otvet2.place(x=225, y=105)
answer_2 = Label(window, text='', font=('Arial', 10, 'bold'))
answer_2.place(x=265, y=105)

def max_degree():
    a = txt_3.get()
    N = int(a)
    degree = 1
    while (2 ** (degree + 1)) <= N:
        degree += 1
    answer_3.configure(text = degree)

tsk3 = Label(window, text='3) По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.\nВыведите показатель степени и саму степень. Операцией возведения в степень пользоваться нельзя!', font=("Arial", 11, 'bold'))
tsk3.place(x=10, y=130)
t3 = Label(window, text='Введите N:')
t3.place(x=10, y=175)
txt_3 = Entry(window, width=10)
txt_3.place(x=80, y=175)
btn3 = Button(window, text='Решить', command=max_degree)
btn3.place(x=170, y=171)
otvet3 = Label(window, text='Ответ: ')
otvet3.place(x=225, y=175)
answer_3 = Label(window, text='', font=('Arial', 10, 'bold'))
answer_3.place(x=265, y=175)

def day():
    a = txt_41.get()
    X = int(a)
    b = txt_42.get()
    Y = int(b)
    day_number = 1
    while Y > (X * 1.1):
        day_number += 1
        X *= 1.1
    answer_4.configure(text = day_number)

tsk4 = Label(window, text='4) В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. По данному числу y определите номер дня, \nна который пробег спортсмена составит не менее y километров. Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.', font=("Arial", 11, 'bold'))
tsk4.place(x=10, y=205)
t4 = Label(window, text='Введите X, Y:')
t4.place(x=10, y=255)
txt_41 = Entry(window, width=10)
txt_41.place(x=90, y=255)
txt_42 = Entry(window, width=10)
txt_42.place(x=150, y=255)
btn4 = Button(window, text='Решить', command=day)
btn4.place(x=225, y=251)
otvet4 = Label(window, text='Ответ: ')
otvet4.place(x=285, y=255)
answer_4 = Label(window, text='', font=('Arial', 10, 'bold'))
answer_4.place(x=330, y=255)

count = 0
def numbers():
    global count
    a = txt_5.get()
    S = int(txt_5.get())
    while int(txt_5.get()) != 0:
        count += 1
        txt_5.delete(0, 'end')
    else:
        answer_5.configure(text = count)
        txt_5.delete(0, 'end')

tsk5 = Label(window, text='5) Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке. Последовательность завершается числом 0, при считывании \nкоторого программа должна закончить свою работу и вывести количество членов последовательности (не считая завершающего числа 0). Числа, следующие за числом 0, считывать не нужно.', font=("Arial", 11, 'bold'))
tsk5.place(x=10, y=280)
t5 = Label(window, text='Введите целые цисла:')
t5.place(x=10, y=330)
txt_5 = Entry(window, width=10)
txt_5.place(x=140, y=330)
btn5 = Button(window, text='Решить', command=numbers)
btn5.place(x=215, y=326)
otvet5 = Label(window, text='Ответ: ')
otvet5.place(x=280, y=330)
answer_5 = Label(window, text='', font=('Arial', 10, 'bold'))
answer_5.place(x=320, y=330)

l = 0
sum = 0
def average_value():
    global l
    S = txt_6.get()
    print(S)
    global sum
    if S != "0":
        l += 1
        sum += int(S)
    else:   
        answer_6.configure(text = sum / (l + 1))        
    txt_6.delete(0,END)


tsk6 = Label(window, text='6) Определите среднее значение всех элементов последовательности, завершающейся числом 0.', font=("Arial", 11, 'bold'))
tsk6.place(x=10, y=360)
t6 = Label(window, text='Введите целые цисла:')
t6.place(x=10, y=390)
txt_6 = Entry(window, width=10)
txt_6.place(x=140, y=391)
btn6 = Button(window, text='Решить', command=average_value)
btn6.place(x=215, y=387)
otvet6 = Label(window, text='Ответ: ')
otvet6.place(x=280, y=390)
answer_6 = Label(window, text='', font=('Arial', 10, 'bold'))
answer_6.place(x=320, y=390)

window.mainloop()