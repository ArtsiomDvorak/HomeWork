# -*- coding: utf-8 -*-
"""Задание_2_со_звездочкой.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KVo8kdJEASzsSUe1M1jGvv-Kl0OykwN3
"""

word = input('Введите прямоугольник, треугольник или круг: ')

if word == 'прямоугольник':
  side_1 = input('Введите сторону a: ')
  side_2 = input('Введите сторону b: ')
  plpr = int(side_1) * int(side_2)
  print('Площадь прямоугольника равна', plpr, 'см^2')
elif word == 'треугольник':
  base = input('Введите основание a: ')
  height = input('Введите высоту h: ')
  pltr = int(0.5 * int(base) * int(height))
  print('Площадь треугольника равна', pltr, 'см^2')
elif word == 'круг':
  radius = input('Введите радиус круга: ')
  plkr = int(3.14 * int(radius)**2)
  print('Площадь круга равна', plkr, 'см^2')
else:
  print('Нужно вводить прямоугольник, треугольник или круг')