def digital_root(n):
    digits_sum = sum([int(num) for num in str(n)])
    return digital_root(digits_sum) if digits_sum > 9 else digits_sum

print(digital_root(16))
print(digital_root(493193))