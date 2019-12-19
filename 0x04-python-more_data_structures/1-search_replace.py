#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new_list = []
        for el in my_list:
            if el == search:
                new_list.append(replace)
            else:
                new_list.append(el)
        return new_list
