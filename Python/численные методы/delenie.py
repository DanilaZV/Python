"""
Используем метод половинного деления для 
нахождения корней уравнения.
"""

import math


def half_interval(a, b):
    """Метод делит интервал по полам"""
    return (a + b) / 2


def get_parametr():
    """Получить данные от пользователя"""
    a = int(input("Введите точку a :"))
    b = int(input("Введите точку b :"))
    E = float(input("Введите точность E:"))

    print('a = {a} Тип:{a1}\nb = {b} Тип {b1}\nE = {E} Тип:{E1}'
      .format(a=a, a1=type(a), b=b, b1=type(b), E=E, E1=type(E))
      )
    return a, b, E


def func(x):
    """
    Вычисляем значение функции, в качестве примера
    2 cos x -7x = 0
    """
    return x*x*x*x - x - 1 #x*x*x-12*(x*x)+6


def start():
    """
    Старт программы
    """
    a, b, E = get_parametr()
    counter = 0
    max_counter = 200

    while abs(b - a) > E:

        counter += 1
        if counter >= max_counter:
            print('Слишком много шагов')
            break

        if abs(b - a) <= E:
            print('Значение math.abs(b-a) стало меньше чем E')
            break

        print('\n\nШаг №{counter}'.format(counter=counter))

        fa = func(a)
        c = half_interval(a, b)
        fc = func(c)
        if fa * fc >= 0:
            a = c
        else:
            b = c
        print('fa = {f_a} fc = {f_c} fa * fc = {res}'.format(f_a=fa, f_c=fc, res=fa * fc))
        print('a = {a} b = {b} c = {c}'.format(a=a, b=b, c=c))


# Запуск программы
start()