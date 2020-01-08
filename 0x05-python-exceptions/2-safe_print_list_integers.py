#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
        printed = 0
        for i in range(x):
                isint = False
                outr = True
                try:
                        isint = isinstance(my_list[i], int)
                except:
                        outr = True
                        pass
                #print(isint)
                if isint is True or outr is True:
                        try:
                                print("{:d}".format(my_list[i]), end="")
                                printed += 1
                        except Exception as e:
                                if type(e).__name__ != "IndexError":
                                                pass
                                else:
                                        raise
                                        exit()
        print()
        return printed
