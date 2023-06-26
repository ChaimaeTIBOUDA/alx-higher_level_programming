#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = []
    for i in range(0, list_length):
        try:
            d = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            d = 0
        except ZeroDivisionError:
            print("out of range")
            d = 0
        finally:
            n.append(d)
    return (n)
