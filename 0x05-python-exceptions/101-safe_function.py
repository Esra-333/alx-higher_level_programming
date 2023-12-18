#!/usr/bin/python3
from __future__ import print_function
from sys import stderr


def safe_function(fct, *args):
    try:
        ret = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return ret
