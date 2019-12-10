#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 is 0 and i % 5 is not 0:
            print("Fizz{spc}".format(spc=" " if i < 100 else ""), end='')
        elif i % 5 is 0 and i % 3 is not 0:
            print("Buzz{spc}".format(spc=" " if i < 100 else ""), end='')
        elif i % 5 is 0 and i % 3 is 0:
            print("FizzBuzz{spc}".format(spc=" " if i < 100 else ""), end='')
        else:
            print("{}{spc}".format(i, spc=" " if i < 100 else ""), end='')
