def dvoika(n):
    n2_str = ''
    while True:
        n_temp = n % 2
        n //= 2
        n2_str += str(n_temp)
        
        if n == 0:
            break

    return n2_str[::-1]


print('Ваше двоичное число:',dvoika(int(input('Введите десятичное число: '))))