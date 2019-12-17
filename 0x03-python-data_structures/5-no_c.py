#!/usr/bin/python3
def no_c(my_string):
    li = list(my_string)
    for i, chara in enumerate(li):
        if chara == 'c' or chara == 'C':
            del li[i]
    return "".join(li)
