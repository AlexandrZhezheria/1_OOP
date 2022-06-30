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

class Salon(Car):

    def __init__(self):
        cars = []
        cars.append(x)

        print(f"1 - {car1}  /n 2 - {car2}  /n 3 - {car3}")

        x = input("Выберите машину для покупки: ")
        print(f"Поздравляем! Вы купили {x} С Вас {self.price} грн.")

    # def car_list(self):
    #     self.car_list()
Salon(Car)





