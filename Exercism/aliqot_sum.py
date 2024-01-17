def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    factors = {1}
    root = round(number ** 0.5) + 1
    factor = 2
    while factor != root:
        if number % factor == 0:
            factors |= {number // factor, factor}
        factor += 1
    if sum(factors) < number:
        return "Deficient"
    if sum(factors) > number:
        return "Abundant"
    return "Perfect"

print(classify(100000000000))