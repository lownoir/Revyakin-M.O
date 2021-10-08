# -*- coding: utf-8 -*-
# Проверить, что поступающего зовут не Иван.

print("Сколько вам лет?")
age = int(input())
print("Как вас зовут?")
name = str(input())

if (age > 0 and age <75 and name != "Иван"):
    if age >= 16:
        print("Поздравляем вы поступили в ВГУИТ")
    else:
        print("Сначала нужно окончить школу!")
else:
    print("Некорректные данные!")