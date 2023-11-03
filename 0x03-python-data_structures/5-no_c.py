#!/usr/bin/python3

def no_c(my_string):

    for c in my_string:
        if c == 'c' or c == 'C':
            modify = my_string.replace('c', "").replace('C', "")

    return modify
