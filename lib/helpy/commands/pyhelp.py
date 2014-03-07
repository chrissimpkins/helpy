#!/usr/bin/env python
# encoding: utf-8

import sys

def print_help_for(the_object):
    try:
        needle = the_object
        if needle.startswith("'") and needle.endswith("'"):
            needle = needle[1:-1]
        elif needle.startswith('"') and needle.endswith('"'):
            needle = needle[1:-1]
        help(needle)
    except Exception as e:
        sys.stderr.write("helpy : There was an error processing the query.")
        sys.exit(1)

