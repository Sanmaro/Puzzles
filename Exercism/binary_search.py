def find(search_list, value):
    while len(search_list) != 0:
        middle_index = len(search_list) // 2
        middle_value = search_list[middle_index]
        if middle_value > value:
            search_list = search_list[:middle_index]
        elif middle_value < value:
            search_list = search_list[middle_index + 1:]
        else:
            return middle_value
    return "not in the list"


print(find([1, 3, 4, 6, 8, 9, 11], 10))