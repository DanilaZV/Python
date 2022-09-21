class User():
    counterr = 0
    """"Класс для пользователей сайта"""
    def __init__(self, login, password, counter):
        """Ициализация атрибутов: логин, пароль"""
        self.login = login
        self.password = password
        self.counter = counter

    def vxod(self):
        """Метод для входа в аккаунт"""
        print('Вы вошли в аккаунт :)')
        self.counter += 1 #Счетчик, считающий кол-во входов
        print(self.counter)
        return self.counter #Возвращает счетчик

    def vblxod(self):
        """Метод для выхода из аккаунта"""
        print('Вы вышли из аккаунта :(')

    def counter1(self):
        """Метод, выводящий количество входов"""
        User.counterr = self.counter
        print('Количество ваших входов: ' + str(User.counterr))

class Priviligies():
    """Вспомогательный класс с привилегиями"""
    def __init__(self, priviligies = []):
        self.priviligies = priviligies
        

class Admin(User):
    """Дочерний класс администратор"""
    def __init__(self, login, password, counter):
        super().__init__(login, password, counter)
        self.priviligies = Priviligies()

    def show_priviligies(self):
        print('Администратов имеет такие привелегии как:')
        for privelege in self.priviligies:
            print(privelege)


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