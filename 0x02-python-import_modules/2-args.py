#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    plural_s = 's' if argc != 1 else ''

    print("Number of argument{}: {}".format(plural_s, argc), end="")
    print("{}".format("s" if argc != 1 else ""), end="")
    print("{}".format(":" if argc > 0 else "."))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))
