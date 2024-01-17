import re

def is_valid(isbn):
    code = "".join(isbn.split("-"))
    if re.fullmatch(r"[0-9]{9}[0-9|X]", code):
        chars = [char if char.isdigit() else 10 for char in code]
        check = 0
        for char, num in zip(chars, range(10, 0, -1)):
            check += int(char) * num
        return check % 11 == 0
    return False

print(is_valid("3-598-21508-8"))