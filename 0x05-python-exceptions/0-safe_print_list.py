#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    tot = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            tot = tot + 1
        except:
            pass

    print()
    return tot
