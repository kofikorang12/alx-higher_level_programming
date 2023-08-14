#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    trueorfalse = []
    for i in my_list:
        if i % 2 == 0:
            trueorfalse.append(True)
        else:
            trueorfalse.append(False)
    return trueorfalse
