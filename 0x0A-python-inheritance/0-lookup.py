#!/usr/bin/python3
"""Module to lookup for available mtds"""


def lookup(obj):
    """
    Returns the list of available attributes and metds of an obj

    Args:
        obj (object): the given obj

    Returns:
        (list): obj list

    """
    return dir(obj)
