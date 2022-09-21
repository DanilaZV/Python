a = input()
b = input()
f1 = open(a, encoding='utf-8')
f2 = open(b, 'w+', encoding='utf-8')
f2.write(*f1)

f1.close()
f2.close()
