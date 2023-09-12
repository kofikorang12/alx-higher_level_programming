#!/usr/bin/python3
''' function containing read_file '''


def read_file(filename=""):
    ''' reads a file '''
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
