#24 вариант. 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Содержимое первого файла:
#Элементы кратные 3:
#Произведение элементов:
#Минимальный элемент:
#Содержимое второго файла:
#Элементы кратные 5:
#Количество элементов:
#Среднее арифметическое элементов:

import random

list_1 = [random.randint(-30, 20) for i in range(random.randint(-10, 10), random.randint(11, 30))]
list_2 = [i for i in list_1 if i > 0]
list_3 = [i for i in list_1 if i < 0]

# Файл 1
f1 = open('file_1.txt', 'w', encoding = 'UTF-8')
f1.write(f"положительные {str(list_2)}\n")
f1.write(f"отрицательные {str(list_3)}\n")
f1.close()

# Файл 2
list_4 = [random.randint(-30, 20) for i in range(random.randint(-10, 10), random.randint(11, 30))]
list_5 = [i for i in list_4 if i > 0]
list_6 = [i for i in list_4 if i < 0]

f1 = open('file_2.txt', 'w', encoding = 'UTF-8')
f1.write(f"положительные {str(list_5)}\n")
f1.write(f"отрицательные {str(list_6)}\n")
f1.close()

# Файл 3
p = 1
f2 = open('file_3.txt', 'w', encoding = 'UTF-8')
f2.write(f"Содержимое первого файла: {str(list_1)}\n")
f2.write(f"Элементы кратные 3: {[i for i in list_1 if i % 3 == 0]}\n")
f2.write(f"Произведение элементов: {[p*k for k in list_1]}\n")
f2.write(f"Минимальный элемент: {[min(list_1)]}\n")

c = 0
for k in list_1:
    c += k
f2.write(f"\nСодержимое второго файла: {str(list_4)}\n")
f2.write(f"Элементы кратные 5: {[i for i in list_4 if i % 5 == 0]}\n")
f2.write(f"Количество элементов: {len(list_4)}\n")
f2.write(f"Среднее арифметическое элементов: {c / len(list_4)}\n")
f2.close()