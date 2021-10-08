# -*- coding: utf-8 -*-
# Переменная seconds хранит в себе некоторое количество секунд. Переведите это число в дни:часы:минуты:секунды.

print("Введите количество секунд:")
seconds = int(input())

days = seconds // 86400
hours = seconds % 86400 // 3600
minutes = seconds % 86400 % 3600 // 60
sec = seconds % 86400 % 3600 % 60

print (days,":",hours,":",minutes,":",sec)