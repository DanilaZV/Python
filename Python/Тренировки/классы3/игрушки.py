class Toy():
    """Класс про игрушки"""
    def __init__(self, price=100, quantity=1, size='little'):
        """Инициализация компонентов: Цена(по умолчанию равна 100), Количество(по умолчанию равен 1) и Размер(по умолчанию равен little)"""
        self.price = price
        self.quantity = quantity
        self.size = size

    def get_price(self):
        """Метод для вызова цены"""
        print(f'Цена данной игрушки равна: {self.price} рублей')

    def get_quantity(self):
        """Метод для вызова количества"""
        print(f'Количество данных игрушек равно: {self.quantity}')

    def get_size(self):
        """Метод для вызова размера"""
        print(f'Размер данной игрушки равен: {self.size}')

    def total_price(self):
        """Метод для подсчёта общей цены"""
        print(f'Цена всех выбранных игрушек составляет: {self.quantity * self.price} рублей')

#Экземпляры класса
toy1 = Toy(1000, 2, 'medium')
toy2 = Toy()
#Выполнение методов класса для экземпляра Toy1
print('Toy1')
toy1.get_price()
toy1.get_quantity()
toy1.get_size()
toy1.total_price()
#Выполнение методов класса для экземпляра Toy2
print('Toy2')
toy2.get_price()
toy2.get_quantity()
toy2.get_size()