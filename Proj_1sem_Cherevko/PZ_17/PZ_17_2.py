#24 вариант. Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
#Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
#"Человек". Каждый класс должен иметь метод, который выводит информацию о поле объекта.

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "male")

    def get_gender(self):
        print("мужчина")

class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "female")

    def get_gender(self):
        print("женщина")

man = Man("Александр", 30)
woman = Woman("Виктория", 25)

man.get_gender()
woman.get_gender()
