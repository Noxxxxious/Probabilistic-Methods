import numpy as np
import random

probability_matrix = np.array([[0.2, 0.1, 0.0, 0.05],
                               [0.0, 0.1, 0.0, 0.05],
                               [0.05, 0.0, 0.1, 0.0],
                               [0.05, 0.0, 0.1, 0.2]])

horizontal = sum(probability_matrix[i, :] for i in range(4))
vertical = [[probability_matrix[j][i] for i in range(4)] for j in range(4)]
for i in reversed(range(4)):
    for j in range(i):
        horizontal[i] += horizontal[j]
for i in range(4):
    for j in range(4):
        for p in range(i + 1, 4):
            vertical[i][j] += probability_matrix[p][j]

result = [[0 for _ in range(4)] for _ in range(4)]
for _ in range(10000):
    rand = np.random.random()
    for i in range(4):
        if rand < horizontal[i]:
            rand = np.random.uniform(0, vertical[0][i])
            for j in reversed(range(4)):
                if rand < vertical[j][i]:
                    result[j][i] += 1
                    break
            break

for line in result:
    print(line)
