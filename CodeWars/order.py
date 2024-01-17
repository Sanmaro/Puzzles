def order(sentence):
    splitted = sentence.split()
    ordered = splitted.copy()
    for word in splitted:
        for char in word:
            if char.isdigit():
                ordered[int(char)-1] = word
                break
    return " ".join(ordered)


def unique_in_order(sequence):
    return "".join(sequence[i] for i in range(len(sequence)) 
                   if i==0 or sequence[i] != sequence[i-1])




print(unique_in_order("AAAABBBCCDAABBB"))

print(order("th1is 5ed ed2 dsdf3 ef4df"))