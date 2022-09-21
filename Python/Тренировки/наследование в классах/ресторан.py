

class Restoran():
    """Класс ресторан"""
    def __init__(self, portion, size, cuisine, price, temperature):
        """Инициализация атрибутов: порция, размер, кухня, цена, температура"""
        self.portion = portion
        self.size = size
        self.cuisene = cuisine
        self.price = price
        self.temperature = temperature

    def posadka(self):
        """Объявление о посадочных местах"""
        print('Появилось свободное место!!!')

    def time_work(self, time): #время от 0 до 24
        """Время работы заведения"""
        if 0 < time < 20:
            print('Открыто')
        else:
            print('Закрыто')

    def employees(self):
        """Количество сотрудников"""    
        print('Количество сотрудников равно', 10)

class Tobacco_varieties():
    """Вспомогательный класс для сортов табака"""
    def __init__(self, virginia='virginia', burley='Burley'):
        self.virginia = virginia
        self.burley = burley

    def order_hook(self):
        """Заказ кальяна"""
        print('Я хочу заказать данный сорт табака: ' + str(self.burley))

class Hookah(Restoran):
    """"""
    def __init__(self, portion, size, cuisine, price, temperature):
        super().__init__(portion, size, cuisine, price, temperature)
        self.virginia = Tobacco_varieties()

    def prosto(self):
        print('Е-маё')
        
 

#Borsch = Restoran(1, 'Большой', 'Русская', 250, 40)
#Borsch.posadka()
#Borsch.employees()
#Borsch.time_work(10)

Pchel = Hookah(1, 'Большой', 'Русская', 250, 40)
Pchel.virginia.order_hook()
Pchel.prosto()