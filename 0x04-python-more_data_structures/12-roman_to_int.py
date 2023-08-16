#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is not True:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    tot = 0
    prev = 0
    for let in roman_string:
        if let not in roman:
            return 0
        if roman[let] > tot:
            tot = roman[let] - tot
        elif roman[let] > prev:
            tot = tot + roman[let] - prev * 2
        else:
            tot = roman[let] + tot
        prev = roman[let]
    return tot
