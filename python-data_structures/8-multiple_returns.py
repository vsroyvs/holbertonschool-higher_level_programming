#!/usr/bin/python3
def multiple_returns(sentence):
    count = len(sentence)
    if count > 0:
        f_c = sentence[0]
    else:
        return (None)
    tupla = (count, f_c)
    return (tupla)
