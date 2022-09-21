class Car():
    """Класс про авто"""
    def __init__(self, color='', type='', year=2000):
        """Инициализация компонентов: цвет(по умолчанию нету), тип(по умолчанию нету) и год(по умолчанию 2000)"""
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        """Метод для запуска авто"""
        print('Автомобиль запущен и готов к работе')

    def distart(self):
        """Метод для прекрашения работы авто"""
        print('Автомобиль заглушен')

    def set_year(self, year):
        """Метод для установки даты производства авто"""
        self.year = year
        print(f'Год выпуска данного автомобиля - {year}')
    
    def set_type(self, type):
        """Метод для утановки типа авто"""
        self.type = type
        print(f'Тип этой машины - {type}')

    def set_color(self, color):
        """Метод для установки цвета авто"""
        self.color = color
        print(f'Данное авто покрашено в {color} цвет')
    
#Экземпляры класса
car1 = Car()
car2 = Car()
#Выполнение  методов
print('Машина 1')
car1.start()
car1.distart()
car1.set_year(2021)
car1.set_type('Кроссовер')
car1.set_color('красный')
print('Машина 2')
car2.set_year(1945)
car2.set_type('Танк')
car2.set_color('камуфляжный')
