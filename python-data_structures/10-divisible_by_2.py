#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list2 = my_list[:]
    list_boolean = []
    for i in list2:
        if i % 2 == 0:
            list_boolean.insert(i, True)
        else:
            list_boolean.insert(i, False)
    return (list_boolean)
