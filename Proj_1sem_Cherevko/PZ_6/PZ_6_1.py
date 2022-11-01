#вариант 24. дан список ненулевых целых чисел размера N. Проверить, образуют ли его элементы геометрическую прогрессию.
#Если образуют, то вывести знаменатель прогрессии, если нет - вывести 0.

import random

N = int(input('Введите размер списка:'))
A = random.randrange(-10,10)
D = random.randrange(-10,10)
print("N = ", N)
print("A = ", A)
print("D = ", D)

a = [A * (D**i) for i in range(N)]
print(a)

D = []
for i in range(0,len(a)-1):
    D.append(a[i+1] / a[i])
min_D = min(D)
max_D = max(D)

if int(round(min_D - max_D)) == 0:
    print("знаменатель прогрессии:", min_D)
else:
    print("0")