#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    div = 0
    for tup in my_list:
        if len(tup) != 2:
            return 0
        num = num + tup[0] * tup[1]
        div = div + tup[1]
    if div == 0:
        return 0
    return num / div
