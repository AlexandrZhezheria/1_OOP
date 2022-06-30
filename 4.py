"""
Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список автомобилей, доступных для
продажи, и функцию продажи заданного автомобиля.
"""


class Car:

    def __init__(self, company, model_name, price):
        self.company = company
        self.model_name = model_name
        self.price = price


car1 = Car('Honda', 'Jazz', 900000)
car2 = Car('Suzuki', 'Alto', 450000)
car3 = Car('BMW', 'X5', 9000000)

print(f"1 - {car1}  \n2 - {car2}  \n3 - {car3}")


class Salon(Car):
    cars = [car1, car2, car3]

    x = input("Выберите машину для покупки: ")

    if x in cars:
        print(f"Поздравляем! Вы купили {x} С Вас {self.price} грн.")
