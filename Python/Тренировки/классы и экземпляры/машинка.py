#Делаем машинку

class Car():
    """Класс по созданию автомобиля"""
    def __init__(self, make, model, year):
        """Ициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def description_name(self):
        """Возращаем описание автомобиля"""
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()
    
    def read_odometer(self):
        """Выводим пробег авто"""
        print("Пробег этого авто " + str(self.odometer_reading) + "км")

    def update_odometer(self, km):
        """Устанавливаем значение на одометре"""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("Не страдай фигней")

    def increment_odometer(self, km):
        """Увелечение показания одометра на заданную величину(Нужно придумать условие)"""
        if km >= 0: #Если пробег будет отрицательным, то программа выведет старый пробег, т.к. это невозможно
            self.odometer_reading += km
        else:
            print('Законы логики нарушаешь!')

my_car = Car('Audi', "a4", 2020)
my_car.update_odometer(60)
my_car.update_odometer(70)
my_car.increment_odometer(100)
my_car.read_odometer()