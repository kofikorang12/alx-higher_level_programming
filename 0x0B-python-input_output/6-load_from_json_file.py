#!/usr/bin/python3
''' function with object creation '''

import json


def load_from_json_file(filename):
    ''' returns object created from json file '''
    with open(filename, 'r') as f:
            my_obj = json.load(f)
    return my_obj
