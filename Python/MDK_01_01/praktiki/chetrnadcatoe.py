from random import randint
n = int(input())
a = 11
 
x = [i for i in range(n)]
#print(x)
 
y = [i for i in x if i % 11 == 0]
print(y)