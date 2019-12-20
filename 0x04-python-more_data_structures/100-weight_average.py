#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) > 0:
        score = 0
        average = 0
        for tup in my_list:
            score = score + (tup[0] * tup[1])
            average = average + tup[1]
        return score / average
    return 0
