from bitarray import bitarray
from bitarray.util import ba2int
a = 69069
c = 1
M = pow(2, 31) - 1
p = 7
q = 3


def new_rand(num):
    return (a * num + c) % M


def xor(b1, b2):
    if (b1 == 0 and b2 == 1) or (b1 == 1 and b2 == 0):
        return 1
    return 0


arr1 = [0] * 10
rand_num = 15

for _ in range(100000):
    rand_num = new_rand(rand_num)
    arr1[10 * rand_num // M] += 1

print(arr1)

arr2 = [0] * 10
rand_bits = [0] * 24
rand_bits.extend([1, 0, 1, 1, 0, 1, 0])

for _ in range(100000):
    for i in range(24):
        rand_bits[i] = xor(rand_bits[i + p], rand_bits[i + q])
    ba = bitarray(rand_bits)
    rand_num2 = ba2int(ba)
    arr2[10 * rand_num2 // M] += 1
    for i in range(6):
        rand_bits[i + 25] = rand_bits[i]

print(arr2)
