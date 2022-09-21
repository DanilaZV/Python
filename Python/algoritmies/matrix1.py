import random

def transpose(matrix):
    matrix[:] = tuple(zip(*matrix))

m = int(input('m = '))
n = int(input('n = '))

Matrix = [ [ random.randint(0, 101) for j in range(n)] for i in range(m) ]
print('Матрица:')


for line in Matrix:
    print(*line)

matrix = Matrix
transpose(matrix)
print('Транспонированая матрица:')
for line in matrix:
    print('   ',*line)