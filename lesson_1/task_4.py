# -*- coding: utf-8 -*-
"""Задание_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UHaBgkx_FAfWb6nXPk9os-OIAzmrZ7Ls
"""

number = input()

even = 0
odd = 0

for i in number:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print('Even:', even, 'Odd:', odd)