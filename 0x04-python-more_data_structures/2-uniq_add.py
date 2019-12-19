#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i, el in enumerate(my_list):
        sum = sum + el
        for j in range(i + 1, len(my_list)):
            if el == my_list[j]:
                my_list[j] = 0
    return sum
