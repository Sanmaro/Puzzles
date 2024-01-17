# def scramble(s1, s2):
#     for char in s2:
#         if char in s1:
#             s1 = s1.replace(char, "", 1)
#             continue
#         return False
#     return True


# Optimized solution
from collections import Counter
def scramble(s1, s2):
    return not Counter(s2) - Counter(s1)



s1 = "gzotcuthvjkzpikz"
s2 = "hpcktzzkjgktu"

print(scramble(s1, s2))
print(scramble('rkqodlw', 'world'))