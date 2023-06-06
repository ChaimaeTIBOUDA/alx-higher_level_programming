#!/usr/bin/python3
for d in range(0, 10):
    for d1 in range(d + 1, 10):
        if d1 == 8 and d1 == 9:
            print("{}{}".format(d, d1))
        else:
            print("{}{}".format(d, d1), end=", ")
