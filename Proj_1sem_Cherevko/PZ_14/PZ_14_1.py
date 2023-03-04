#24 вариант. В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя
#(например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать
#количество полученных элементов.

import re
a = open('Dostoevsky.txt', 'r', encoding='utf-8')
b = a.read()

answer = 0
x = re.findall(r'\d{4}', b)
year = re.findall(r'\d{4}.*года|\d{4}.*году|\d{4}.*годе|\d{4}.*год', b)
k = len(x)
k1 = len(year)

print('Все элементы:', x)
print('Кол-во всех элементов:', k)
print('Элементы без повторений:', year)
print('Кол-во элементоов без повторений:', k1)
