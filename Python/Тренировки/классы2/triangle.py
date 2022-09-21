#Класс треугольника
class Triangle():
    """Класс для теругольника"""
    def __init__(self):
        pass

    def triangle_checker(self, a, b, c):
        """"Метод для проверки на существование треугольника(попроще)"""
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
            if a > 0 and b > 0 and c > 0:
                if a + b > c and a + c > b and b + c > a:
                    return print('Ура, можно построить теругольник')
                return print('Жаль, но из этого треугольника не сделать.')
            return print('С отрицательными числами ничего не выйдет!')
        return print('Нужно вводить только числа!')
        
triangle1 = Triangle()
triangle1.triangle_checker(30.6, 40.7, 50.8)
triangle1.triangle_checker(20, 40.7, 50.8)
triangle1.triangle_checker(-30.6, 40.7, 50.8)
triangle1.triangle_checker('30.6', 40.7, 50.8)