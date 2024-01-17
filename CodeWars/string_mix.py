from collections import Counter
def mix(s1, s2):
    s1_count = Counter(s1.replace(" ","")).most_common()
    s2_count = Counter(s2.replace(" ","")).most_common()
    result = ""
    for i in range(min(len(s1_count), len(s2_count))):
        letter1, num1, letter2, num2 = s1_count[i][0], s1_count[i][1], \
            s2_count[i][0], s2_count[i][1]
        if letter2.islower() and letter2 in s1_count:
            if num1 > num2:
                result += f"1:{letter1*num1}/"
            elif num1 < num2:
                result += f"2:{letter2*num2}/"
            else:
                result += f"=:{letter1*num1}/"
    return result              


    # for i in range(min(len(s1_count), len(s2_count))):
    #     letter1, num1, letter2, num2 = s1_count[i][0], s1_count[i][1], \
    #         s2_count[i][0], s2_count[i][1]
    #     if letter1.islower() and letter2.islower():
    #         if num1 > num2:
    #             result += f"1:{letter1*num1}/"
    #         elif num1 < num2:
    #             result += f"2:{letter2*num2}/"
    #         else:
    #             result += f"=:{letter1*num1}/"
    return result

print(mix("Are they here", "yes, they are here"))