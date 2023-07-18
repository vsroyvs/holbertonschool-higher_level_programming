#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if a_dictionary is None:
        return None
    else:
        for k, v in a_dictionary.items():
            if v > max:
                max = v
        return max
