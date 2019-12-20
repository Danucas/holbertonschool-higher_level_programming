#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        highest = 0
        k = ''
        for key in a_dictionary:
            if a_dictionary[key] > highest:
                highest = a_dictionary[key]
                k = key
        return k
