#!/usr/bin/python3
def test():
    a = 1024
    print(id(a))
    b = 1024
    print(id(a))
    del a
    del b
    c = 1024
    print(id(c))

test()
import dis

dis.dis(test)
