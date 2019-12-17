#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        flag = my_list[0]
        for num in my_list:
            if num > flag:
                flag = num
        return flag
