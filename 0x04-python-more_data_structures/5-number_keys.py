#!/usr/bin/python3
def number_keys(a_dictionary):
    sum_num = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        sum_num += 1

    return (sum_num)
