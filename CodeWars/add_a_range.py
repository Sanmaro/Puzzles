def get_sum(a,b):
    return sum(range(a, b + 1)) if a < b else sum(range(b, a + 1))

print(get_sum(0, 5))