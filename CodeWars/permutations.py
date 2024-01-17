import itertools

def permutations(s):
    permuts = set((itertools.permutations(s)))
    return ["".join(tuple) for tuple in permuts]

print(permutations('aabb'))