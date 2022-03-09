

def permutations(n_set, permutation, depth, perm_count):
    for n in n_set:
        permutation.append(n)
        if depth == len(arr) - 1:
            print(permutation)
            perm_count += 1
        else:
            perm_count = permutations(n_set, permutation, depth + 1, perm_count)
        permutation.pop()
    return perm_count


arr = [1, 2, 3]
perm = list()
print(permutations(arr, perm, 0, 0))
