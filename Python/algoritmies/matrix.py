import random

import numpy as np

def random_matrix(R, cols):

        matrix = []

        rows =  0

        while  rows < cols:

            N = random.sample(R, cols)

            matrix.append(N)

            rows = rows + 1

        return np.array(matrix)

print(random_matrix(range(10), 5))