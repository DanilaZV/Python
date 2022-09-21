#Импортирование разными способами
class Restoran():
    """Класс ресторан"""
    def __init__(self, portion, size, cuisine, price, temperature):
        """Инициализация атрибутов: порция, размер, кухня, цена, температура"""
        self.portion = portion
        self.size = size
        self.cuisene = cuisine
        self.price = price
        self.temperature = temperature

    def zakaz(self):
        """Вывод заказа"""
        print('Количество порций равно ' + str(self.portion) + ';', 'Размер порции равен ' + self.size + ';', 'Блюдо из ' + self.cuisene + ' кухни' + ';', 'Цена за блюдо равняется ' + str(self.price) + ' рублям' + ';', 'Температура при подачи блюда равна ' + str(self.temperature) + ' градусам по шкале Цельсия' + ';', sep='\n')

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




