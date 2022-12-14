#вариант 24. дано множество А из N точек(точки заданы своими координатами x,y). Найти пару различных точек этого
#множества с максимальным расстоянием между ними и само это расстояние(точки выводяися в том же порядке, в котором они
#перечислены при задании множества A). Расстояние R между точками с координатами(x1,y1) и (x2,y2) вычисляется по формуле:
#R=sqrt(x2-x1)^2+(y2-y1)^2. Для хранения данных о каждом наборе точек следует использовать по два списка: первый список
#для хранения абсцисс, второй - для хранения ординат.


import random
import math
def maximum(x1, x2, y1, y2): #функция, которая принимает 4 параметра
    R = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)) #формула по которой находится расстояние
    list_2.append(R)


try:
    c = int(input('Введите число точек в массиве A: ')) #ввод кол-ва точек
    list_2 = []
    list_x = [random.randint(0, 100) for i in range(c)] #добавление в список абсцисс и ординат точек
    list_y = [random.randint(0, 100) for i in range(c)]
    '''Ввод данных пользователем в переменную a,b в int формате'''
except ValueError:  #обработчик исключений, который выводит ошибку, в случае если введённое число c не в int типе
    print('Ошибка')
else: #условие иначе, где выполняется продолжение блока try
    print('Количество всех точке по x в массиве A:', list_x) #вывод списка list_x в котором хрантся все x
    print('Количество всех точке по y в массиве A:', list_y) #вывод списка list_y в котором хрантся все y
    n = 0
    while True:
        if len(list_2) == 1000:
            break
        number = random.randint(0, len(list_x)-1)
        maximum(list_x[number-1], list_x[number], list_y[number-1], list_y[number])
        continue
    while True:  #цикл, в котором проверяются все значения в списке list_2 + max number
        id = random.randint(0, len(list_x)-1)
        if math.sqrt(((list_x[id] - list_x[id-1]) ** 2) + ((list_y[id] - list_y[id-1]) ** 2)) == max(list_2):
            print(f"\n\tПара чисел у которых самое большое расстояние: {list_x[id], list_y[id]}--{list_x[id - 1], list_y[id - 1]}\n\tСамо расстояние: {max(list_2)}")
            break
        else:
            continue