n = int(input())
for i in range(11, n + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)
