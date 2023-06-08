#!/usr/bin/python3
if __ name__ == "__main__":
    import sys
    r = 0
    for j in range(len(sys.argv) - 1):
        r += int(sys.argv[j + 1])
    print("{}".format(r))
