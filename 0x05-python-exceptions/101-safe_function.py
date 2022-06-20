#!/usr/bin/python3
# 101-safe_function.py


import sys


def safe_function(fct, *args):
    """
    A function that executes a function safely
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
