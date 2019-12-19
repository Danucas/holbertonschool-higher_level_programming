#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for el in set_1:
        for comp in set_2:
            if el == comp:
                common.append(el)
    return common
