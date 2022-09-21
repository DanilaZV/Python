number1 = int(input('Введите длину: '))
number2 = int(input('Введите ширину: '))

def square(a):
    n = a*a
    return n

print('Площадь квадрата:', square(number1))

def square(a, p):
    o = a*p
    return o

print('Площадь прямоугольника:', square(number1, number2))