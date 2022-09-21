class MyClass():
    pass

A = MyClass()
B = MyClass()

A.first = 'Экземпляр A'
B.second = 'Экземпляр B'

MyClass.total = 'MyClass'

print(A.total, "->", A.first)
try:
    print(A.second)
except AttributeError:
    print('Такого поля у экземпляра А нет')

class MyClass():
    def say(self):
        print('Всем привет!')

obj = MyClass()
obj.say()

MyClass.say(obj)

MyClass.say('Ку-ку')