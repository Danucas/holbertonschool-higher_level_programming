#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
        printed = 0
        for i in range(x):
                try:
                        printed += 1
                        print("{}".format(str(my_list[i])), end="")
                except:
                        pass
        if printed > 0:
                print()
        return printed
