from fractions import Fraction

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
        self.amount = round(float(self.amount) / snows)

    def Snejok(self, snows):
        Snejok_rows = ('\n'.join([('*' * int(snows)) for _ in range(self.amount)]))
        return Snejok_rows


n = Snow()
print('First snows: %i' % n.amount)
n + 4
print('add 4: %i' % n.amount)
n - 6
print('sub 6: %i' % n.amount)
n / 4
print('truediv 4: %i' % n.amount)
n * 5
print('mul 5: %i' % n.amount)
rectt = n.Snejok(8)
print('8 снежков в %i рядов' % n.amount)
print(rectt)
a = Snow(4)
print('15 снежков в %i ряда' % a.amount)
rectt2 = a.Snejok(15)
print(rectt2)