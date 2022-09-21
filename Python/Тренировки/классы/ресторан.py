#Делаю классы
from os import sep


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Две переменные: Название и Тип кухни"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        #print('Строим свой ресторан')
        
    def describe_restaunt(self):
        """Вывод атрибутов названия и типа кухни"""
        print(self.restaurant_name, self.cuisine_type, sep='\n')

    def open_restaurant(self):
        print("Ресторан открыт!")
# Экземпляры класса
restaurant1 = Restaurant("Клоп Мане", 10)
restaurant2 = Restaurant("По-быстренькому", 1)
restaurant3 = Restaurant("У шеф-повара", 7)
restaurant4 = Restaurant("Итальяно", 9)
# Вызовы экземпляров1
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.describe_restaunt()
restaurant1.open_restaurant()
# Вызовы экземпляров2
restaurant1.describe_restaunt()
restaurant2.describe_restaunt()
restaurant3.describe_restaunt()
restaurant4.describe_restaunt()