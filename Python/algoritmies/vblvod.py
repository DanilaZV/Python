f = open(r'C:\tur\re.txt', encoding='utf-8')
l = [line.strip() for line in f]
print('Текст файла:', l)

a = int(input('Введите номер строки для вывода: ')) - 1
print(l[a])