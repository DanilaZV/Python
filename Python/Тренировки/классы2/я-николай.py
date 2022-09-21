class Nikola():
    __slots__ = ['name', 'age']
    #__slots__ - не позволяет задать новые параметры атрибутов, кроме тех что уже есть.
    def __init__(self, name, age):
        self.name = name
        if self.name != 'Николай':
            self.name = f'Я не {self.name}, а Николай'
        self.age = age

person1 = Nikola('Иван', 31)
person2 = Nikola('Николай', 14)
print(person1.name)
print(person2.name)
person2.surname = 'Петров'