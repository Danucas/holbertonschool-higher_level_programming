#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
        new_list = []
        for i in range(list_length):
                try:
                        res = my_list1[i] / my_list2[i]
                        new_list.append(res)
                except TypeError:
                        print("wrong type")
                except ZeroDivisionError:
                        print("division by 0")
                except IndexError:
                        print("out of range")
                finally:
                        new_list.append(0)
                        pass
        return new_list
