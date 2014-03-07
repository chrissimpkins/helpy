#!/usr/bin/env python
# encoding: utf-8

#------------------------------------------------------------------------------
# Application Name
#------------------------------------------------------------------------------
app_name = 'helpy'

#------------------------------------------------------------------------------
# Version Number
#------------------------------------------------------------------------------
major_version = "1"
minor_version = "0"
patch_version = "1"

#------------------------------------------------------------------------------
# Debug Flag (switch to False for production release code)
#------------------------------------------------------------------------------
debug = False

#------------------------------------------------------------------------------
# Usage String
#------------------------------------------------------------------------------
usage = """
Usage: helpy <module,class,method,function,keyword>
Use --helpy help-- for more information"""

#------------------------------------------------------------------------------
# Help String
#------------------------------------------------------------------------------
help = """
---------------------------------------
 helpy
 Copyright 2014 Christopher Simpkins
 MIT license
---------------------------------------

helpy displays built-in Python documentation from the command line. View documentation by Python module, class, method, function, or keyword.

USAGE

  helpy <module,class,method,function,keyword>

EXAMPLES

  Module Docs ••••••   helpy sys

  Class Docs  ••••••   helpy dict

  Method Docs ••••••   helpy dict.update

  Function Docs  •••   helpy max

SOURCE REPOSITORY

  https://github.com/chrissimpkins/helpy

ISSUE REPORTING

  https://github.com/chrissimpkins/helpy/issues"""
