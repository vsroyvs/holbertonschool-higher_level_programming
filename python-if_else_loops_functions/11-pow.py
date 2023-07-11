#!/usr/bin/python3
def pow(a, b):
    po = 1
    if (b == 0):
        return (1)
    elif (b > 0):
        for i in range(1, b + 1):
            po = po * a
        return (po)
    elif (b < 0):
        for i in range(1, abs(b) + 1):
            po = po * a
        return (1 / po)
