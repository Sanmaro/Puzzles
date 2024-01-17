from functools import reduce

def narcissistic(value):
    return value == reduce(lambda x, y: x + y, [int(dig) ** len(str(value)) for dig in str(value)])

print(narcissistic(371))