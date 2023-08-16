#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return None
    rom = roman_string
    num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_integer = 0
    for i in range(len(roman_string)):
        if roman_string[i] in num:
            if i + 1 < len(rom) and num[rom[i]] < num[rom[i + 1]]:
                roman_integer -= num[roman_string[i]]
            else:
                roman_integer += num[roman_string[i]]
        else:
            return None
    return roman_integer
