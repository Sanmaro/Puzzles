<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> e83ae84f94fa497255de1a9688042684b15ce4b3

def main():
    units = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
        ]
    code = []
    codes = []
    test = []
    with open("D:/Coding/Python/puzzles/AoC/1a.txt") as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            # for unit in units:
            #     if unit in line:
            #         index = line.find(unit) + 1
            #         line = line[:index] + str(units.index(unit) + 1) + line[index+1:]
            for char in line:
                if char.isdigit():
                    code.append(char)
            test.append(line)
            codes.append(code[0] + code[-1])
            code.clear()
    
    codes = list(map(int, codes))
    calibration_code = sum(codes)
    print(calibration_code)


if __name__ == "__main__":
<<<<<<< HEAD
=======
=======

def main():
    units = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
        ]
    code = []
    codes = []
    test = []
    with open("D:/Coding/Python/puzzles/AoC/1a.txt") as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            # for unit in units:
            #     if unit in line:
            #         index = line.find(unit) + 1
            #         line = line[:index] + str(units.index(unit) + 1) + line[index+1:]
            for char in line:
                if char.isdigit():
                    code.append(char)
            test.append(line)
            codes.append(code[0] + code[-1])
            code.clear()
    
    codes = list(map(int, codes))
    calibration_code = sum(codes)
    print(calibration_code)


if __name__ == "__main__":
>>>>>>> 1c4bb1d554e1787639bd741b2ae2402151fd51a2
>>>>>>> e83ae84f94fa497255de1a9688042684b15ce4b3
    main()