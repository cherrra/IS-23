#вариант 24. В матрице найти отрицательные элементы, сформировать из них новый массив. Вывести размер нового массива.
import random
import numpy as np

m = random.randint(2, 6)
n = random.randint(2, 6)
a = np.random.randint(-10, 10, (n, m))

result = a[a < 0]

print('Исходная матрица:\n', a)
print('Размер нового массива:', *result.shape)
print('Новый массив с отрицательныи элементами:', result)