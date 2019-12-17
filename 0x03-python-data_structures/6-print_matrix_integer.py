#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i, el in enumerate(line):
            print("{}".format(el), end='')
            if i < (len(line) - 1):
                print(" ", end='')
        print()
