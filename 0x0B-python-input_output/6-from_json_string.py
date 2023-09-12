#!/usr/bin/python3
''' function with json interpreting '''

import json


def from_json_string(my_str):
    ''' returns object represented my json string '''
    return json.loads(my_str)
