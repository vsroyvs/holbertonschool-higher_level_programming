#!/usr/bin/python3
def multiple_returns(sentence):
    count = len(sentence)
    if count > 0:
        f_c = sentence[0]
    else:
        f_c = "None"
    tupla = (count, f_c)
    return (tupla)
