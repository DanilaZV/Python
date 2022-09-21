from cgi import test
import math
def fixedPoint(f, epsilon):
    guess = 1.0   
    for i in range(100):
        if -epsilon < f(guess) - guess < epsilon:
            return guess
        else:
            guess = f(guess)

def sqrt(a):
    def babylon(x):
        def test(x):
            return 2-x-math.log(x)
        return test(x)

    return fixedPoint(babylon, 0.001)


print(test)