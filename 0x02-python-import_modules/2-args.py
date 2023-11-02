#!/usr/bin/python3

if __name__ == "__main__":
   import sys

    argv = sys.argv
    def printArgs (args):
        argCount = 0
        argsLen = len(args) - 1

        if argsLen == 0:
            print("{} arguments.".format(argsLen))
        elif argsLen == 1:
            print("{} argument:".format(argsLen))
            print("{}: {}".format(argsLen, argv[1]))
        else:
            print("{} arguments:".format(argsLen))
            for arg in argv:
                if arg[0][0] == '.':
                    continue
                argCount += 1
                print("{}: {}".format(argCount, arg))

    printArgs(argv)

