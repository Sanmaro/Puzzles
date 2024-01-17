from random import choice
import string

def generateName():
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    name = [choice(alphabet) for _ in range(6)]
    return "".join(name)

print(generateName())