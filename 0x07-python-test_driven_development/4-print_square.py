#!/usr/bin/python3

def print_square(size):
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for r in range(size):
            for c in range(size):
                print('#', end='')
            print()