import string

def is_pangram(s):
    letters = [char for char in string.ascii_lowercase]
    for char in s:
        if char.lower() in letters:
            letters.remove(char.lower())
    return len(letters) == 0


def is_pangram2(s):
    letters = string.ascii_lowercase
    for char in s.lower():
        if char in letters:
            letters = letters.replace(char, "")
    return len(letters) == 0

print(is_pangram2("abcdefghijklmnopqrstuvwxyz"))


