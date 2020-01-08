#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
        printed = 0
        try:
                for i in range(x):
                        print("{}".format(my_list[i]), end="")
                        printed += 1
                if printed > 0:
                        print()
                return printed
        except IndexError:
                if printed > 0:
                        print()
                return printed
