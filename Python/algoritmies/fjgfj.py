path_to_file = 'C:\tur\re.txt'
a = str(input('Введите слово:'))
#with open(r'C:\tur\re.txt', encoding='utf-8') as file:
    #for line in file:
        #print(line)
file = open(r'C:\tur\re.txt', encoding='utf-8')
text=file.read()
l = [line.strip() for line in file]
if a in text:
    print (a)
    print(l[a])