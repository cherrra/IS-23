#вариант 24. даны целые положительные числа N и K. используя только операции сложения и вычитания, найти частное от деления нацело N на K, а также
#остаток от этого деления

N, K = int(input("введите 1 число:")), int(input("введите 2 число:"))
a = N
b = 0
while a >= K:
    a -= K
    b += 1
print("частное:", b)
print("остаток:", a)