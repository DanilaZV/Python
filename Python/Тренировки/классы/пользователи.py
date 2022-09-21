#Делаю классы
class User():
    def __init__(self, first_name, last_name, age, orientation, date_birth):
        """Переменные: Имя, Фамилия, Возраст, Ориентация, Дата рождения"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.orientation = orientation
        self.date_birth = date_birth
    
    def describe_user(self):
        """Вывод всей информации о пользователях"""
        print(self.first_name, self.last_name, self.age, self.orientation, self.date_birth, sep='\n')

    def greet_user(self):
        """Вывод персонального приветствия"""
        print("Приветствую вас " + self.first_name + "!")

#Экземпляры класса
user1 = User("Ваня", "Хромцов", 17, "ЛЕСБИЯНКА", "01.04.2004")
user2 = User("Никита/Николай", "Шарипов/Шариков", 18, "Натурал", "17.12.2003")
user3 = User("Романус", "Филипповский", 18, "", "28.01.2004")
user4 = User("Антон", "Четырин", 17, "Пидарас", "16.08.2005")
user5 = User("Данила", "Зимин", 17, "Вертолет", "08.08.2004")

#Вызов методов класса
user4.describe_user()
user4.greet_user()