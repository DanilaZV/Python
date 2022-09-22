n, a = int(input()), int(input())

for _ in range(n-1):
    x = [i for i in range(n)]
    #lst.append(a + x)
    a = x
print(x)