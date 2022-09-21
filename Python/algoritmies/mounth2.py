m = ['Январь',28,31,30,31,30,31,31,30,31,30,31]
def f(day):
    month = 0
    for i in m:
        day -= i
        month += 1
        if day <= 0:
            return day+i,month
            
print(f(31))
print(f(40))
print(f(365))