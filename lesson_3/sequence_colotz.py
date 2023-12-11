# -*- coding: utf-8 -*-
"""Последовательность_Колатца.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GwZ2PovBTJfj9kcMVWU7M8bBoUdQkQSG
"""

def sequence_of_colatz(arg_1):
  i = 0
  while arg_1 != 1:
   i += 1
   if arg_1 % 2 == 0:
      arg_1 = arg_1 // 2
   else:
      arg_1 = arg_1 * 3 + 1
  return i

list_1 = []
for i in range(1,1000000):
  a = sequence_of_colatz(i)
  list_1.append(a)
b = max(list_1)
c = list_1.index(b) + 1
print(f'Цепочка: {b}', f'Число: {c}')