import itertools

def middle_permutation(string):
    letters = sorted([letter for letter in string])
    permutations = list(itertools.permutations(letters))
    return "".join(permutations[len(permutations) // 2])

print(middle_permutation("abc"))