def pig_it(text):
    punct = ".,?!"
    splitted = text.split()
    for i, word in enumerate(splitted):
        mark = ""
        if word[-1] in punct:
            mark = word[-1]
            word = word.replace(word[-1], "")
        word += word[0]
        word = word.replace(word[0], "", 1)
        word += "ay" + mark
        splitted[i] = word
    return " ".join(splitted)

print(pig_it('Pig latin is. cool'))

import string