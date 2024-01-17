from string import ascii_letters

def main():
    priorities = [char for char in ascii_letters]
    threefolds = []
    threefold = []
    badges = []
    with open("3.txt") as file:
        rucksacks = [line.strip() for line in file]
        for i in range(0, len(rucksacks), 3):
            for j in range(3):
                threefold.append(rucksacks[i+j])
            threefolds.append(threefold)
            threefold = []

    for elves in threefolds:
        for elf in elves:
            for char in elf:
                if char in elves[1] and char in elves[2]:
                    badges.append(priorities.index(char) + 1)
                    break
            break

    print(sum(badges))



main()