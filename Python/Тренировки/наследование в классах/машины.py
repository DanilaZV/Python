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

class Battery():
    """Простая модель аккумулятора для электромобиля"""
    def __init__(self, battery=100):
        self.battery = battery

    def discharge(self, odometer):
        """Метод по разрядке батареи"""
        self.odometer = odometer
        battery_charge = self.battery - (odometer * 0.1) #90 Кв
        pasxod = (odometer * 0.1)
        print('Вы потратили ' + str(int(pasxod)) + ' Киловатт' + '.','Сейчас заряд вашего автомобиля равен ' + str(int(battery_charge)) + ' Киловатт'+ '.', sep='\n')


    def rangee(self):
        print('На данный момент вы можете проехать ещё ' + str(int((self.battery - (self.odometer * 0.1)) * 10)) + ' Км')

    def zaridka(self):
        """Метод для зарядки батареи до 100%"""
        print(self.battery)

    def upgrade_battery(self):
        """Метод зарядки батареи до 100% №2"""
        if self.battery != 100:
            self.battery = 100

    def description_battery(self):
        """Выводит информацию о мощности батареи"""
        print('Этот автомобиль имеет батарею мощностью ' + str(self.battery) + ' киловатт')

class Electricalcar(Car):
    """Аспекты для электромобиля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов родительского класса"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def description_name(self):
        """Переопределение родительского метода"""
        desc = str(self.year) + ' ' + self.model
        return desc.title()

waitan = Electricalcar('УРАЛ', 'К-110', 1976)
print(waitan.description_name())
waitan.battery.description_battery()
waitan.battery.discharge(100)
waitan.battery.zaridka()
waitan.battery.upgrade_battery()
waitan.battery.zaridka()
waitan.battery.rangee()