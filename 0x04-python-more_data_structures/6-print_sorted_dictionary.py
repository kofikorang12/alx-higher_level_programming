#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_order = list(a_dictionary.keys())
    key_order.sort()
    for i in key_order:
        print("{}: {}".format(i, a_dictionary.get(i)))
