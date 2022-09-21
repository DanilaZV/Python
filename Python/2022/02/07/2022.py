class Snow:
    amount = int()

    def __init__(self, snows = 5):
        self.amount = snows

    def __call__(self, snows):
        self.amount = snows

    def __add__(self, snows):
        self.amount += snows

    def __sub__(self, snows):
        self.amount -= snows

    def __mul__(self, snows):
        self.amount *= snows

    def __truediv__(self, snows):
        self.amount = self.amount / snows

    def MS(self, snows):
        self.snows = ('\n'.join([('*' * snows) for _ in range(int(self.amount))]))
        return self.snows

a = Snow()
print('first snows: %i' % a.amount)
a + 1
print('add 1: %i' % a.amount)
a - 2
print('sub 2: %i' % a.amount)
a / 3
print('truediv 3: %i' % a.amount)
a * 4
print('mul 4: %i' % a.amount)
snow = a.MS(7)
print('makeSnow with 7 * in row and %i rows' % a.amount)
print(snow)
a = Snow(3)
print('makeSnow with 10 * in row and %i rows' % a.amount)
snow2 = a.MS(10)
print(snow2)