class Math():
    """Класс связанный с математикой"""
    def __init__(self, a, b):
        """Инициализация компонентов: a и b"""
        self.a = a
        self.b = b

    def addition(self):
        """Метод для сложения переменных a и b"""
        print(f'Результат сложения равен {self.a + self.b}')

    def multiplicaton(self):
        """Метод для умножения переменных a и b"""
        print(f'Результат умножения равен {self.a * self.b}')

    def division(self):
        """Метод для деления переменных a и b"""
        print(f'Результат деления равен {self.a / self.b}')

    def substraction(self):
        """Метод для вычитания переменных a и b"""
        print(f'Результат вычитания равен {self.a - self.b}')

#Экземпляры класса
Primer1 = Math(10, 5)
Primer2 = Math(100, 65)
Primer3 = Math(2, 3)
Primer4 = Math(16, 20)
#Выполнение методов
print('Первый пример')
Primer1.addition()
Primer1.multiplicaton()
Primer1.division()
Primer1.substraction()
print('Второй пример')
Primer2.division()
print('Третий пример')
Primer3.addition()
print('Четвертый пример')
Primer4.multiplicaton()