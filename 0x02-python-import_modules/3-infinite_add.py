#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv

    result = 0

    for arg in args:
        if arg[0] == '.':
            continue
        result += int(arg)

    print(result)
