#!/usr/bin/env python
# encoding: utf-8

#------------------------------------------------------------------------------
# Application Name
#------------------------------------------------------------------------------
app_name = 'pyh'

#------------------------------------------------------------------------------
# Version Number
#------------------------------------------------------------------------------
major_version = "0"
minor_version = "1"
patch_version = "0"

#------------------------------------------------------------------------------
# Debug Flag (switch to False for production release code)
#------------------------------------------------------------------------------
debug = False

#------------------------------------------------------------------------------
# Usage String
#------------------------------------------------------------------------------
usage = """
Usage: pyh <module,class,method,function,keyword>
Use --pyh help-- for more information"""

#------------------------------------------------------------------------------
# Help String
#------------------------------------------------------------------------------
help = """
---------------------------------------
 pyh
 Copyright 2014 Christopher Simpkins
 MIT license
---------------------------------------

pyh displays built-in Python documentation from the command line. View documentation by Python module, class, method, function, or keyword.

USAGE

  pyh <module,class,method,function,keyword>

EXAMPLES

  Module Docs ••••••   pyh sys

  Class Docs  ••••••   pyh dict

  Method Docs ••••••   pyh dict.update

  Function Docs  •••   pyh max

SOURCE REPOSITORY

  https://github.com/chrissimpkins/pyh

ISSUE REPORTING

  https://github.com/chrissimpkins/pyh/issues"""
