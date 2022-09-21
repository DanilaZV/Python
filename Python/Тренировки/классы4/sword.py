class MightiestWeapon:
    name = "Default name"
    def __init__(self, weapon_type):
        self.weapon_type = weapon_type

#Атрибут name можно переопределить и не создавая объекта
MightiestWeapon.name = 'Stell Sword'
print(MightiestWeapon.name)
#создаем объект и сразу же инициализируем динамический атрибут с помощью конструктора
hero_sword = MightiestWeapon('sword')
# и теперь, уже для конткретного объекта, можно задать имя
hero_sword.name = 'Excalibur'
# новое статическое имя по умолчанию для всего класса не изменится
print(MightiestWeapon.name)
print(hero_sword.name)