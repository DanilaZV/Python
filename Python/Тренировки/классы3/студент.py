class Student():
    """Класс студенты"""
    def __init__(self, name='Ivan', age=18, groupNumber='10A'):
        """Инициализация компонентов: Имя(по умолчанию имя равно Ivan), Возраст(по умолчанию возрас равен 18) и Номер группы(по умолчанию номер группы равен 10А)"""
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        """Метод во выводу имени студента"""
        print(f'Имя выбранного студента: {self.name}')

    def getAge(self):
        """Метод по выводу возраста студента"""
        print(f'Возраст выбранного студента: {self.age}')

    def getGroupNumber(self):
        """Метод по выводу номера группы студента"""
        print(f'Номер группы выбранного студента: {self.groupNumber}')

    def setName(self, name):
        """Метод по замене имени студента"""
        self.name = name
        print(f'Имя студента заменено на {name}')

    def setAge(self, age):
        """Метод по замене возраста студента"""
        self.age = age
        print(f'Возраст студента заменен на {age}')

    def setGroupNumber(self, groupNumber):
        """Метод по замене номера группы студента"""
        self.groupNumber = groupNumber
        print(f'Номер группы изменен на {groupNumber}')

#Экземпляры класса
Vlad = Student("Vlad", 16, "12d")
Misha = Student("Misha", 12, "7a")
Samira = Student("Samira", 10, "10f")
Ivan = Student()
Zoro = Student("Zoro", 20, "12s")
#Использование методов класса
Vlad.setName("Vladimir")
Misha.setAge("15")
Samira.setGroupNumber("10c")
Zoro.setName('Арнольд')
Zoro.setAge(83)
Zoro.setGroupNumber('46N')
print(Ivan.name,Ivan.age)
print(Zoro.name, Zoro.age, Zoro.groupNumber)