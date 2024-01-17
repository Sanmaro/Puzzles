<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> e83ae84f94fa497255de1a9688042684b15ce4b3

# Two 19, at least three 5
def puzzle1():
    numbers = list(map(int, input("Input:\n").split(",")))
    count_19 = 0
    count_5 = 0
    result = "False"
    for number in numbers:
        if number == 19:
            count_19 += 1
        elif number == 5:
            count_5 += 1
        if count_19 == 2 and count_5 > 3:
            result = "True"
            break
    print(f"Output:\n{result }")

# puzzle1()


# Length 8, fifth element 3x
def puzzle2():
    numbers = list(map(int, input("Input:\n").split(",")))
    length = len(numbers)
    fifth = numbers[4]
    result = "False"
    if length == 8 and numbers.count(fifth) == 3:
        result = "True"
    print(f"Output:\n{result}")

# puzzle2()


# Greater than 4^4, 4 modulo 34
def puzzle3():
    number = int(input("Input:\n"))
    result = "False"
    if number > 4 ** 4 and number % 34 == 4:
        result = "True"
    print(f"Output:\n{result}")

# puzzle3()


# Piles of n stones
def puzzle4():
    n = int(input("Input:\n"))
    piles = []
    for i in range(n):
        piles.append(n)
        n += 2
    print(f"Output:\n{piles}")

# puzzle4()


# Second last string is substring of last string
def puzzle5():
    strings = input("Input:\n").split(", ")
    result = "False"
    if strings[-2] in strings[-1]:
        result = "True"
    print(f"Output:\n{result}")

# puzzle5()


# List of 100 elements, each 10 greater than the last
def puzzle6():
    numbers = list(map(int, input("Input:\n").split(",")))
    length = len(numbers)
    result = "False"
    for i in range(1, length):
        if length == 100 and numbers[i] - numbers[i-1] == 10:
            result = "True"
    print(f"Output:\n{result}")

<<<<<<< HEAD
=======
=======

# Two 19, at least three 5
def puzzle1():
    numbers = list(map(int, input("Input:\n").split(",")))
    count_19 = 0
    count_5 = 0
    result = "False"
    for number in numbers:
        if number == 19:
            count_19 += 1
        elif number == 5:
            count_5 += 1
        if count_19 == 2 and count_5 > 3:
            result = "True"
            break
    print(f"Output:\n{result }")

# puzzle1()


# Length 8, fifth element 3x
def puzzle2():
    numbers = list(map(int, input("Input:\n").split(",")))
    length = len(numbers)
    fifth = numbers[4]
    result = "False"
    if length == 8 and numbers.count(fifth) == 3:
        result = "True"
    print(f"Output:\n{result}")

# puzzle2()


# Greater than 4^4, 4 modulo 34
def puzzle3():
    number = int(input("Input:\n"))
    result = "False"
    if number > 4 ** 4 and number % 34 == 4:
        result = "True"
    print(f"Output:\n{result}")

# puzzle3()


# Piles of n stones
def puzzle4():
    n = int(input("Input:\n"))
    piles = []
    for i in range(n):
        piles.append(n)
        n += 2
    print(f"Output:\n{piles}")

# puzzle4()


# Second last string is substring of last string
def puzzle5():
    strings = input("Input:\n").split(", ")
    result = "False"
    if strings[-2] in strings[-1]:
        result = "True"
    print(f"Output:\n{result}")

# puzzle5()


# List of 100 elements, each 10 greater than the last
def puzzle6():
    numbers = list(map(int, input("Input:\n").split(",")))
    length = len(numbers)
    result = "False"
    for i in range(1, length):
        if length == 100 and numbers[i] - numbers[i-1] == 10:
            result = "True"
    print(f"Output:\n{result}")

>>>>>>> 1c4bb1d554e1787639bd741b2ae2402151fd51a2
>>>>>>> e83ae84f94fa497255de1a9688042684b15ce4b3
# puzzle6()