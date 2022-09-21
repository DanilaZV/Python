# класс "Животное". Это достточчно абстрактный класс всего с одним методом "Издать звук".
class Animal():
    def make_a_sound(self):
        print('Издаёт животный звук')
# факт наследования в Python указывается при объявлении класса-наследника.
# в скобках, после имени класса, указывается класс родитель.
class Cat(Animal):
    def drop_everything(self):
        print('Вставай скорее, я всё уронил!')

class Dog(Animal):
    def dig_the_ground(self):
        print('Однажды я докопаюсь до ядра планеты!')

# отныне для объектов класса "Собака" будет выполняться именно эта реализация метода.
    def make_a_sound(self):
        print('Гав-Гав!')

Tom = Cat()
Tom.make_a_sound()
Tom.drop_everything()

Reks = Dog()
Reks.make_a_sound()
Reks.dig_the_ground()