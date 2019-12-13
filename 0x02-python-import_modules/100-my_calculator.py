#!/usr/bin/python3
def checkdigits(number):
    for digit in number:
        digit = ord(digit)
        if digit >= 48 and digit <= 57:
            continue
        else:
            return False
    return True


def exit(filename, sys):
    print('Usage: {} <a> <operator> <b>'.format(filename))
    sys.exit(1)


def main():
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    argc = len(argv)
    if argc != 4:
        exit(argv[0], sys)
    else:
        op = argv[2]
        if checkdigits(argv[1]) is False or checkdigits(argv[3]) is False:
            exit(argv[0], sys)
        a = int(argv[1])
        b = int(argv[3])
        if op == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif op == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif op == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif op == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, *, and /")
            sys.exit(1)

if __name__ == '__main__':
    main()
