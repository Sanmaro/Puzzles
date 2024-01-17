import string

# Part 1
def part1():
    parts = []
    part = ""
    specials = list(string.punctuation)
    specials.remove(".")
    with open("3.txt") as file:
        engine = [list(line[:-1]) for line in file]

    for i in range(len(engine)):
        for j in range(len(engine[i])):
            try:
                if (engine[i][j].isdigit() 
                and (engine[i][j-1] in specials
                or engine[i][j+1] in specials
                or engine[i-1][j-1] in specials
                or engine[i-1][j] in specials
                or engine[i-1][j+1] in specials
                or engine[i+1][j-1] in specials
                or engine[i+1][j] in specials
                or engine[i+1][j+1] in specials)):
                    try:
                        if (engine[i][j-2].isdigit()
                        and engine[i][j-1].isdigit()):
                            part += engine[i][j-2]
                            engine[i][j-2] = "x"
                        if engine[i][j-1].isdigit():
                            part += engine[i][j-1]
                            engine[i][j-1] = "x"
                    except IndexError:
                        pass
                    part += engine[i][j]
                    engine[i][j] = "x"
                    try:
                        if engine[i][j+1].isdigit():
                            part += engine[i][j+1]
                            engine[i][j+1] = "x"
                            if engine[i][j+2].isdigit():
                                part += engine[i][j+2]
                                engine[i][j+2] = "x"
                    except IndexError:
                        pass
                    parts.append(part)
                    part = ""
            except IndexError:
                pass
    parts = list(map(int, parts))
    print(sum(parts)) 


# Part 2
def part2():
    parts = []
    part = ""
    star = "*"
    with open("3_test.txt") as file:
        engine = [list(line[:-1]) for line in file]

    for i in range(len(engine)):
        for j in range(len(engine[i])):
            try:
                if (engine[i][j] == star 
                and 
                ((engine[i][j-1].isdigit()
                or engine[i][j+1].isdigit()
                or engine[i-1][j-1].isdigit())
                and 
                (engine[i-1][j].isdigit()
                or engine[i-1][j+1].isdigit())):
                    try:
                        if (engine[i][j-3].isdigit()
                        and engine[i][j-2].isdigit()
                        and engine[i][j-1].isdigit()):
                            part += engine[i][j-3]
                            engine[i][j-2] = "x"
                        if (engine[i][j-2].isdigit()
                        and engine[i][j-1].isdigit()):
                            part += engine[i][j-2]
                            engine[i][j-1] = "x"
                        if engine[i][j-1].isdigit():
                            part += engine[i][j-1]
                            engine[i][j-1] = "x"
                    except IndexError:
                        pass

                or
                ((engine[i-1][j].isdigit()
                or engine[i-1][j+1].isdigit())
                and
                (engine[i+1][j-1].isdigit()
                or engine[i+1][j].isdigit()
                or engine[i+1][j+1].isdigit()))
                or
                ((engine[i][j-1].isdigit()
                or engine[i][j+1].isdigit()
                or engine[i-1][j-1].isdigit())
                and
                (engine[i+1][j-1].isdigit()
                or engine[i+1][j].isdigit()
                or engine[i+1][j+1].isdigit()))):
                    try:
                        if (engine[i][j-2].isdigit()
                        and engine[i][j-1].isdigit()):
                            part += engine[i][j-2]
                            engine[i][j-2] = "x"
                        if engine[i][j-1].isdigit():
                            part += engine[i][j-1]
                            engine[i][j-1] = "x"
                    except IndexError:
                        pass
                    part += engine[i][j]
                    engine[i][j] = "x"
                    try:
                        if engine[i][j+1].isdigit():
                            part += engine[i][j+1]
                            engine[i][j+1] = "x"
                            if engine[i][j+2].isdigit():
                                part += engine[i][j+2]
                                engine[i][j+2] = "x"
                    except IndexError:
                        pass
                    parts.append(part)
                    part = ""
            except IndexError:
                pass
    parts = list(map(int, parts))
    print(sum(parts)) 

# part1()
part2()