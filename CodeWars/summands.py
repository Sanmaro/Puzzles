def two_sum(numbers, target):
    for i, first in enumerate(numbers):
        for j, second in enumerate(numbers[i+1:], start=1):
            if first + second == target:
                return (i, i+j)
            
print(two_sum([6, 5, 2, 2, 3], 4))