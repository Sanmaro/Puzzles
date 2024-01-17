import re

def to_camel_case(text):
    camel = (re.split(r"_|-", text)[0] 
        + "".join(word.capitalize() for word in re.split(r"_|-", text)[1:]))
    return camel


def solution(s):
    s_decamel = [char if char.islower() else (" " + char) for char in s]
    return "".join(s_decamel)

print(solution("breakCamelCase"))