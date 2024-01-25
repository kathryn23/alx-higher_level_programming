#!/usr/bin/python3
def complex_delete(a_dict, value):
    copy = a_dict.copy()
    for i, j in copy.items():
        if value in j:
            del a_dict[k]
    return a_dict
