#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    n_list = sorted(a_dictionary)
    for i in n_list:
        print("{}: {}".format(i, a_dictionary[i]))
