class Rectangle():
    """Класс прямоугольник"""
    def __init__(self, width, height):
        """Инициализация компонентов: ширина, длина"""
        self.width = width
        self.height = height

    def get_width(self):
        """Вывод ширины"""
        return self.width

    def get_height(self):
        """Вывод длины"""
        print(self.height)

    def area(self):
        """Вывод площади"""
        return self.width * self.height

#Экземпляры класса
r1 = Rectangle(10, 5)
r2 = Rectangle(20, 11)

#Использование методов
print(r1.width)
print(r1.height)
print(r1.get_width())
print(r1.area())
r1.get_height()

print('Second Rectangle')

print(r2.width)
print(r2.height)
print(r2.get_width())
print(r2.area())
r2.get_height()