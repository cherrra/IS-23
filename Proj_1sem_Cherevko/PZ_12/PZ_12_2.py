#вариант 24. Составить список, в который будут включены только согласные буквы и привести их к верхнему регистру.
#Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']

lst = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
vse_sogl = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
sogl = [k.upper() for i in range(len(lst)) for k in lst[i] if k.lower() in vse_sogl]
print(sogl)