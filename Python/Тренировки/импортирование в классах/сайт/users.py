from user import *
from admin import *


#Экземпляры класса
admin1 = Admin('Admin', 123, 0)
user1 = User('Данила', 1111111, 0)
user2 = User('Антон', 1111112, 0)
user3 = User('Иван', 1111113, 0)

#Вызов методов
admin1.priviligies = ['Создание постов','Удаление постов','Бан пользователя']
admin1.show_priviligies()
user1.vxod()
user1.vblxod()
user1.vxod()
user1.vblxod()
user1.vxod()
user1.vblxod()
user1.counter1()