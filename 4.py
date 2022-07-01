"""
Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список автомобилей, доступных для
продажи, и функцию продажи заданного автомобиля.
"""


class Car:
    def __init__(self, brand, color, price, model):
        self.brand = brand
        self.color = color
        self.price = price
        self.model = model


class Salon:
    def __init__(self, cars):
        self.cars = cars

        self.show()

    def show(self):
        global flag

        flag = False

        for car in self.cars:
            print(f"{self.cars.index(car) + 1}.) {car.brand} {car.model} with {car.color} color and price = "
                  f"{car.price}$")
            flag = True

    def sell(self, number_of_car):
        car = self.cars[number_of_car - 1]

        print(f"\nThe car {car.brand} {car.model} was sold!\n")

        del self.cars[number_of_car - 1]


car1 = Car("Mercedes", "green", 100000, "S-Class")
car2 = Car("BMW", "green", 70000, "i8")
car3 = Car("Toyota", "green", 30000, "Camry")
car4 = Car("Chevrolet", "green", 80000, "Camaro")
car5 = Car("Porsche", "green", 20000000, "911")

flag = True

salon = Salon([car1, car2, car3, car4, car5])

while flag:
    buy = int(input("\nWhich number to you want to buy?: "))

    salon.sell(buy)
    salon.show()



