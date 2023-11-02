#!/usr/bin/python3

#if __name__ == "__main__":
#   import sys

#    argv = sys.argv
#    def printArgs (args):
#        argCount = 0
#        argsLen = len(args) - 1

#        if argsLen == 0:
#            print("{} arguments.".format(argsLen))
#        elif argsLen == 1:
#            print("{} argument:".format(argsLen))
#            print("{}: {}".format(argsLen, argv[1]))
#        else:
#            print("{} arguments:".format(argsLen))
#            for arg in argv:
#                if arg[0][0] == '.':
#                    continue
#                argCount += 1
#                print("{}: {}".format(argCount, arg))

#    printArgs(argv)

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = len(sys.argv) - 1
    if total == 0:
        print("0 arguments.")
    elif total == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(total))
    for p in range(total):
        print("{}: {}".format(p + 1, sys.argv[p + 1]))
