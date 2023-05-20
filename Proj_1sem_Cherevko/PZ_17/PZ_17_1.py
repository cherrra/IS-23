#24 вариант. Создайте класс "Компьютер" с атрибутами "марка", "процессор", "оперативная память".
#Напишите метод, который выводит информацию о компьютере  формате "Марка: марка,
#Процессор: процессор, Оперативная память: память"

class Computer:
    def __init__(self, brand, processor, memory):
        self.brand = brand
        self.processor = processor
        self.memory = memory

    def info(self):
        print(f"Марка: {self.brand}, Поцессор: {self.processor}, Оперативная память: {self.memory}")

mycomp = Computer('Asus', 'Intel Core', '8 Gb')
mycomp.info()