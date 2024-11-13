from datetime import datetime

class Car:
    __number_of_cars = 0
    
    def __init__(self, brand, model, year) -> None:
        self.__brand = brand
        self.__model = model
        self.__year = year
        Car.__number_of_cars +=1

    def age_of_car(self):
        return datetime.now().year - self.__year
    @classmethod
    def total_cars(cls):
        return Car.__number_of_cars

    def car_info(self):
        print(f"Brand: {self.__brand}, Model: {self.__model}, Year: {self.__year}")


class ElectricCar(Car):

    def __init__(self, brand, model, year, battery_life) -> None:
        super().__init__(brand, model, year)
        self.__battery_life = battery_life

    def battery_info(self):
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.__battery_life} საათი")
    

print(Car.total_cars())