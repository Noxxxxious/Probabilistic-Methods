import random
import math

N = 10000
numbers = [random.random() for i in range(N)]
prob = [0, 0.2, 0.6, 0.75, 1]
for i in range(len(numbers)):
    for j in range(1, len(prob)):
        if prob[j - 1] < numbers[i] < prob[j]:
            numbers[i] = j

p = [0 for i in range(4)]
for i in range(N):
    p[numbers[i] - 1] += 1
print(p)


numbers2 = [100 * random.random() + 50 for i in range(N)]
p2 = [0 for i in range(10)]
for i in range(N):
    index = math.floor(numbers2[i]/10) - 5
    p2[index] += 1
print(p2)
