#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k in a_dictionary:
        if k == key:
            del(a_dictionary[key])
        else:
            break
    return a_dictionary
