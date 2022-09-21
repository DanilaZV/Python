class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.2046

    @property
    #Декоратор. Метод получатель
    def kg(self):
        return self.__kg

    @kg.setter
    #Метод установщик
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')
    

#Экземпляры класса
vec100 = KgToPounds(100)
print(vec100.to_pounds())
print(vec100.kg)
vec100.kg = 111111
print(vec100.to_pounds())
print(vec100.kg)
vec100.kg = 'luk'
#weight = KgToPounds(12)
#print(weight.to_pounds())
#print(weight.kg)
#weight.kg = 41
#print(weight.kg)
#weight.kg = 'десять'