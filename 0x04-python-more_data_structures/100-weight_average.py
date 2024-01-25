#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    num = 0
    den = 0

    for element in my_list:
        num += element[0] * element[1]
        den += element[1]

    return (num / den)
