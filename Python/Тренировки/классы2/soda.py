#Класс Сода(напиток)
class Soda():
    """Создание класса сода для лимонадов"""
    def __init__(self, impurity):
        """Инициализация компонентов: добавка(примесь) в соду"""
        if isinstance(impurity, str):
            # isinstance - в данном случае определяет к какому типу данных относится объект
            self.impurity = impurity
        else:
            self.impurity = None

    def show_my_drink(self):
        """Метод добавляющий добавку или без неё"""
        if self.impurity:
            print(f'Газировка и {self.impurity}')
        else:
            print('Обычная газировка')

#Экземпляры класса
Drunker = Soda('Лёд')
Drunker1 = Soda('Виски')
Drunker2 = Soda('Кола')
Drunker3 = Soda(4)
Drunker4 = Soda(None)
#Выполнение методов
Drunker.show_my_drink()
Drunker1.show_my_drink()
Drunker2.show_my_drink()
Drunker3.show_my_drink()
Drunker4.show_my_drink()