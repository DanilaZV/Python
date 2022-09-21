num = str(input()) 

with open(r"C:\tur\re.txt", encoding='utf_8') as f:
    lst = f.readlines()

for i in lst:
    if num in i:
        print(i)