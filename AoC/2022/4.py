from csv import reader

def main():
    useless = 0
    with open("4.csv") as file:
        sections = list(reader(file))

    for section in sections:
        for subrange in section:
            section[section.index(subrange)] \
                = list(range(int(
                    subrange.split("-")[0]), 
                    int(subrange.split("-")[1]) + 1))
            
    for section in sections:
        if (section[0] in section[1]) \
        or (section[1] in section[0]):
            useless += 1
    print(useless)


main()