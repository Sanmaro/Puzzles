<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> e83ae84f94fa497255de1a9688042684b15ce4b3
# Reverse letters in each word
def puzzle1():
    # words = input("Input: ").split()
    words = "Ja jsem tady. A taky tady.".split()
    interpunction = ".?!"
    words_reversed = []
    for word in words:
        inter = False
        if any(item in word for item in interpunction) == True:
            words_reversed.append(word[-2::-1] + word[-1])
            continue
        words_reversed.append(word[::-1])
    print(" ".join(words_reversed))

# puzzle1()


# Read txt file and replace newline with whitespace
def puzzle2():
    text = []
    with open("test.txt") as file:
        for line in file:
            line = line.replace("\n", " ")
            text.append(line)
    print(*text)

# puzzle2()


# Remove integers greater than 50 from list
def puzzle3():
    integers = [10, 20, 30, 40, 50, 60, 20, 70, 80, 90, 50, 100]
    for i in range(len(integers) - 1, -1, -1):
        if integers[i] > 50:
            integers.remove(integers[i])
    print(integers)

puzzle3()
<<<<<<< HEAD
=======
=======
# Reverse letters in each word
def puzzle1():
    # words = input("Input: ").split()
    words = "Ja jsem tady. A taky tady.".split()
    interpunction = ".?!"
    words_reversed = []
    for word in words:
        inter = False
        if any(item in word for item in interpunction) == True:
            words_reversed.append(word[-2::-1] + word[-1])
            continue
        words_reversed.append(word[::-1])
    print(" ".join(words_reversed))

# puzzle1()


# Read txt file and replace newline with whitespace
def puzzle2():
    text = []
    with open("test.txt") as file:
        for line in file:
            line = line.replace("\n", " ")
            text.append(line)
    print(*text)

# puzzle2()


# Remove integers greater than 50 from list
def puzzle3():
    integers = [10, 20, 30, 40, 50, 60, 20, 70, 80, 90, 50, 100]
    for i in range(len(integers) - 1, -1, -1):
        if integers[i] > 50:
            integers.remove(integers[i])
    print(integers)

puzzle3()
>>>>>>> 1c4bb1d554e1787639bd741b2ae2402151fd51a2
>>>>>>> e83ae84f94fa497255de1a9688042684b15ce4b3
