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
        print(self.battery)

    def description_battery(self):
        """Выводит информацию о мощности батареи"""
        print('Этот автомобиль имеет батарею мощностью ' + str(self.battery) + ' киловатт')