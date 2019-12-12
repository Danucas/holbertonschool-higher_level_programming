#!/usr/bin/python3
import hidden_4


def main():
    for m in dir(hidden_4):
        if str(m)[0] != "_":
            print(m)


if __name__ == '__main__':
    main()
