<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> e83ae84f94fa497255de1a9688042684b15ce4b3
def main():
    with open("1.txt") as file:
        elves = [line.rstrip() for line in file]

    breakpoint = ""
    result = []
    temp_list = []

    for calory in elves:
        if calory == breakpoint:
            result.append(temp_list)
            temp_list = []
        else:
            temp_list.append(calory)

    result.append(temp_list)
    elves.clear()

    for elf in result:
        elf = sum(list(map(int, elf)))
        elves.append(elf)

    most_calories = []
    for i in range(3):
        most_calories.append(max(elves))
        elves.remove(max(elves))
    print(sum(most_calories))

if __name__ == "__main__":
<<<<<<< HEAD
=======
=======
def main():
    with open("1.txt") as file:
        elves = [line.rstrip() for line in file]

    breakpoint = ""
    result = []
    temp_list = []

    for calory in elves:
        if calory == breakpoint:
            result.append(temp_list)
            temp_list = []
        else:
            temp_list.append(calory)

    result.append(temp_list)
    elves.clear()

    for elf in result:
        elf = sum(list(map(int, elf)))
        elves.append(elf)

    most_calories = []
    for i in range(3):
        most_calories.append(max(elves))
        elves.remove(max(elves))
    print(sum(most_calories))

if __name__ == "__main__":
>>>>>>> 1c4bb1d554e1787639bd741b2ae2402151fd51a2
>>>>>>> e83ae84f94fa497255de1a9688042684b15ce4b3
    main()