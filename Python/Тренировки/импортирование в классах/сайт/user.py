#Импортирование разными способами
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

