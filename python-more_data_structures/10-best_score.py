#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = 0
    for key, value in a_dictionary.items():
        if max == 0 or value > a_dictionary[max]:
            max = key
    return max
