#вариант 24. даны целые числа A и B(A < B). вывести все целые числа от A до B включительно; при этом число А должно выводиться 1 раз, А+1 2 раза и т.д.
A, B = int(input("введите 1 число:")), int(input("введите 2 число:"))
k = 1
for i in range (A, B+1):
    for j in range(0,k):
        print(i, end=" ")
    print()
    k += 1