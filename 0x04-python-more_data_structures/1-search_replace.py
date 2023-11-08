#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if search not in my_list:
        return my_list

    new_list = my_list.copy()

    for s_item in new_list:
        if search == s_item:
            new_list[new_list.index(s_item)] = replace

    return new_list
