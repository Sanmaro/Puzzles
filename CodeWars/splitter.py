def strip_comments(strng, markers):
    lined = strng.split("\n")
    for i, line in enumerate(lined):
        for mark in markers:
            if mark in line:
                line = line[:line.find(mark)]
            lined[i] = line
    return "\n".join(lined)

print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))