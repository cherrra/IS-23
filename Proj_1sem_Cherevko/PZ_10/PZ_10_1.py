#вариант 24. в магазинах имеются следующие товары. магнит - молоко, соль, сахар. пятерочка - мясо, молоко, сыр.
#опеределить: 1) какие товары из магнита отсутствуют в пятерочке; 2) какие товары из пятерочки отсутствуют в магните;
#3) полный перечень всех товаров; 4) равны ли перечни товаров.

magnit = {'сахар', 'соль', 'молоко'}
pyterochka = {'молоко', 'мясо', 'сыр'}

print('Товары из магнита, отсутствующие в пятерочке:', magnit - pyterochka)
print('Товары из пятерочки, отсутсвующие в магните:', pyterochka - magnit)
print('Полный перечень всех товаров:', magnit|pyterochka)
print('Равны ли перечни товаров:', magnit == pyterochka)