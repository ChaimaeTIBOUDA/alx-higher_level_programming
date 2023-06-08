#!/usr/bin/python3

def magic_calculation(x, y):
    from magic_calculation_102 import add, sub
    if x < y:
        j = add(x, y)
        for i in range(4, 6):
            j = add(j, i)
        return j
    else:
        return sub(x, y)
