#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    count = len(my_list)
    if (idx < 0):
        return my_list
    elif(idx > count):
        return my_list
    else:
        new_list[idx] = element
        return (new_list)
