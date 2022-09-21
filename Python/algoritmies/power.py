def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return power(a, n - 1) * a
    else:
        a2 = power(a, n // 2)
        return a2 * a2

number = int(input('Введите число: '))
ppower = int(input('Введите степень числа: '))

print(power(number, ppower))

