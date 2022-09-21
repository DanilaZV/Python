from car import Car
from battery import Battery

class Electricalcar(Car):
    """Аспекты для электромобиля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов родительского класса"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def description_name(self):
        """Переопределение родительского метода"""
        desc = str(self.year) + ' ' + self.model
        return desc.title()
