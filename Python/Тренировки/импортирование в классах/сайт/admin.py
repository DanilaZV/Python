from user import User

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