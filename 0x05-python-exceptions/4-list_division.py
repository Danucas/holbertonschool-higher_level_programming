#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
        new_list = []
        try:
                for i in range(list_length):
                        try:
                                res = my_list1[i] / my_list2[i]
                                new_list.append(res)
                        except TypeError:
                                new_list.append(0)
                                print("wrong type")
                        except ZeroDivisionError:
                                new_list.append(0)
                                print("division by 0")
        except IndexError:
                print("out of range")
        finally:
                return new_list
