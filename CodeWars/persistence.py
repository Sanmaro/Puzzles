from functools import reduce

def persistence(n):
    count = 0
    while n > 9:
        n = reduce(lambda x, y: x * y, [int(dig) for dig in str(n)])
        count += 1
    return count

print(persistence(39))