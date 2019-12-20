#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = {}
    for key in list(a_dictionary.keys()):
        if isinstance(a_dictionary[key], type(value)):
            if isinstance(a_dictionary[key], list) is not True \
               and a_dictionary[key] == value:
                del a_dictionary[key]
            else:
                new_dic[key] = a_dictionary[key]
        else:
            new_dic[key] = a_dictionary[key]
    return new_dic
