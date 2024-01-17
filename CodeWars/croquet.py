def open_or_senior(data):
    output = []
    for person in data:
        if person[0] >= 55 and person[1] > 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))