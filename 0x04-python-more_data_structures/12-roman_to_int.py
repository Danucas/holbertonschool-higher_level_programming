#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    if type(roman_string) is str:
        for i, char in enumerate(roman_string):
            if i < len(roman_string) - 1:
                nex = roman_string[i + 1]
                if nex in romans:
                    n = romans[nex]
                    if n > romans[char] and n < (romans[char] * 100):
                        sum = sum - romans[char]
                    else:
                        sum = sum + romans[char]
                elif char in romans:
                    sum = sum + romans[char]
        return sum
    return 0
