#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = [d[x] for x in roman_string] + [0]
    r = 0
    for i in range(len(n) - 1):
        if n[i] >= n[i + 1]:
            r += n[i]
        else:
            r -= n[i]
    return r
