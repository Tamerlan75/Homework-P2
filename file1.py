# 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input("Введите количетво монеток: "))
# e = 0
# t = 0
# for i in range(n):
#     p = int(input("Введите положение монетки: "))
#     if p == 1:
#         e+= 1
#     if p == 0:
#         t += 1
# if e < t:
#     print(e)
# else:
#     print(t)

# 2. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input("Введите число N: "))
# k =1
# p = 0
# while p<=n:
#     p = 2**k
#     if p < n:
#         print(p)
#         k+=1
