#24 вариант. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
import random

n = random.randint(2, 6)
m = random.randint(2, 6)
a = [[random.randint(-10, 10) for j in range(n)] for i in range(m)]

print('Исходная матрица:\n', a)
print(*('среднее арифметическое {} = {}'.format(x, sum(x)/len(x)) for x in a[::2]), sep='\n')