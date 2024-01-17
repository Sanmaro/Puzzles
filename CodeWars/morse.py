def decode_morse(morse_code):
    MORSE_CODE[""] = " "
    MORSE_CODE["  "] = " "
    decoded = [MORSE_CODE[char] for char in morse_code.split(" ")]
    return "".join(decoded)

print(de)