def mounth(a):
    if a in [4, 6 ,9, 11]:
        n = 30
        return n
    elif a == 2:
        n = 28
        return n
    else:
        n = 31
        return n

c = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]
b = int(input("Введите число: "))
mounth1 = 1
while b > mounth(mounth1):
    b = b - mounth(mounth1)
    mounth1 += 1
    if mounth1 > 12:
        mounth1 = 1

mounth1 -= 1
print(b, c[mounth1])