#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = len(my_list)
    if (count == 0):
        return
    for i in reversed(range(count)):
        print("{:d}".format(my_list[i]))
