def first_non_repeating_letter(s):
    res_letter = s[0]
    for first in s:
        for second in s[s.find(first) + 1:]:
            if first.lower() == second.lower():
                break
        else:
            res_letter = first
            break
    return res_letter



import re

def increment_string(strng):
    splitted = re.match(r"([0-9]+)(.+)?", strng[::-1])
    if splitted:
        num, word = splitted.group(1)[::-1], splitted.group(2)[::-1]
        return f"{word}{str(int(num) + 1).zfill(len(num))}"
    return f"{strng}1"

print(increment_string("09"))