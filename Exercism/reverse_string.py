import timeit
from functools import wraps
    
def timing(func):
    """Include debug statement and timeit setup"""
    @wraps(func)
    def wrapper(*args):
        res = func(*args)
        print(res)
        times = timeit.repeat(
            stmt=lambda: func(*args),
            repeat=1, number=10000)
        print(times)
    return wrapper

@timing
def comprehension_reverse(word):
    output = "".join([word[i] for i in range(len(word) - 1, -1, -1)])
    return output

@timing
def slice_reverse(word):
    output = word[::-1]
    return output

@timing
def loop_reverse(word):
    output = ""
    for i in range(len(word) - 1, -1, -1):
        output += word[i]
    return output

@timing
def smart_reverse(word):
    output = list(word)
    length = len(word)
    for i in range(length // 2):
        output[i], output[length - 1 - i] = output[length - 1 - i], output[i]
    return "".join(output)

word = "".join(map(str, list(range(100))))

print(comprehension_reverse(word))
print(slice_reverse(word))
print(loop_reverse(word))
print(smart_reverse(word))