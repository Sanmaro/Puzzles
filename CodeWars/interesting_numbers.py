def is_interesting(number, awesome_phrases):   
    interests = []
    if is_three_up(number) == 0:
        return 0
    elif is_three_up(number) == 1:
        return 1

    for i in range(3):
        if i == 0:
            interests.append(is_zeros(number))
            interests.append(is_same_digits(number))
            interests.append(is_ascend(number))
            interests.append(is_descend(number))
            interests.append(is_palindrom(number))
            interests.append(is_awesome(number, awesome_phrases))
        elif (
            is_zeros(number + i) == 2
            or is_same_digits(number + i) == 2
            or is_ascend(number + i) == 2
            or is_descend(number + i) == 2
            or is_palindrom(number + i) == 2
            or is_awesome(number + i, awesome_phrases)
                ):
            interests.append(1)

    return 2 if 2 in interests else 1 if 1 in interests else 0


def is_three_up(number):
    return 0 if number < 98 else 1 if 89 <= number < 100 else None


def is_zeros(number):
    if number % (10 ** (len(str(number))-1)) != 0:
        return 0
    return 2


def is_same_digits(number):
    div = -1
    while div != 0:
        div, mod = divmod(number, 10)
        if mod != (div % 10) and div != 0:
            return 0
        number = div
    return 2


def is_ascend(number):
    div = -1
    while div != 0:
        div, mod = divmod(number, 10)
        if (((mod - 1) != (div % 10) 
            and div != 0
            and mod != 0) 
            or (mod == 0 and (div % 10) != 9)
            ):
            return 0
        number = div
    return 2


def is_descend(number):
    div = -1
    while div != 0:
        div, mod = divmod(number, 10)
        if (mod + 1) != (div % 10) and div != 0:
            return 0
        number = div
    return 2


def is_palindrom(number):
    num_str = str(number)
    if num_str != num_str[::-1]:
        return 0
    return 2


def is_awesome(number, awesome):
    if number not in awesome:
        return 0
    return 2
    



print(is_interesting(67890, [1337, 256]))