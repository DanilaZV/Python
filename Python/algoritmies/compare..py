def comparison(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

print(comparison(number1, number2))