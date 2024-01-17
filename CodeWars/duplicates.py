def duplicate_count(text):
    duplicates = {}
    for i, first in enumerate(text):
        for j, second in enumerate(text):
            if (first == second) and (i != j):               
                duplicates[first] = 1
    return len(duplicates)
     

print(duplicate_count("abcdeaa"))