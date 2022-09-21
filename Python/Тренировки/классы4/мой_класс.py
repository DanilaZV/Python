# Создаем класс
class MyClass():
    # Создаем поле класса
    name = 'класс MyClass'
    # Метод для присваивания значения полю экземпляра класса
    def set(self, n):
        self.nickname = n
    # Метод для отображения значения поля экземпляра класса
    def get(self):
        print('Значение поля', self.nickname)
    def __init__(self, n):
        # Полю экземпляра класса присваевается значение
        self.set(n)
        print('Создан экземпляр класса')
        self.get()

green = MyClass('Зеленый')
print('Принадлежность:', green.name)

red = MyClass('Красный')
print('Принадлежность', red.name)

# Присваивание полю класса значение
MyClass.name = 'Здесь могла быть ваша реклама'
print('Спрашивает Зеленый', green.name)
print('Спрашивает красный', red.name)
green.name = 'Здесь рекламы не будет'
print(green.name)
print(red.name)