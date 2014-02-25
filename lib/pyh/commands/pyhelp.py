#!/usr/bin/env python
# encoding: utf-8

def print_help_for(the_object):
    needle = the_object
    if needle.startswith("'") and needle.endswith("'"):
        needle = needle[1:-1]
    elif needle.startswith('"') and needle.endswith('"'):
        needle = needle[1:-1]
    help(needle)

