#!/usr/bin/python3


def uniq_add(my_list=[]):
    if not my_list or len(my_list) == 0:
        return []
    my_set = set(my_list)
    res = 0
    for i in my_set:        
        res = res + i

    return res
