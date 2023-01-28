#вариант 24. Даны значения роста 20 юношей.
#Определить сколько юношей будут направлены в баскетбольную команду (рост от 190) и сколько в футбольную (остальные).

from random import randint
lst = [randint(150, 231) for i in range(20)]
basket = [i for i in lst if i >= 190]
football = [i for i in lst if i < 190]
print(lst)
print('Кол-во юношей, попавших в баскетбольную команду:', len(basket))
print('Кол-во юношей, попавших в футбольную команду:', len(football))

