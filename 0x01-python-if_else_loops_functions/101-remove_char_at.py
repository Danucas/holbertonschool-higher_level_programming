#!/usr/bin/python3
def remove_char_at(str, n):
    pos = 0
    res_arr = []
    for char in str:
        if pos is not n:
            res_arr.append(char)
        pos += 1
    return "".join(res_arr)
