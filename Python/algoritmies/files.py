word = 'вторая'
 
with open(r'C:\tur\re.txt', encoding='utf-8') as f:
    for line in f:
        if word in f:
            print(f)