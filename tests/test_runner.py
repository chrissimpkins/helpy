#!/usr/bin/env python
# encoding: utf-8

import unittest
from pyh.commands.pyhelp import print_help_for
from Naked.toolshed.shell import muterun
from Naked.toolshed.state import StateObject
import subprocess

class PyHelpTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_execute_command(self):
        state = StateObject()
        if (state.py_major == 2 and state.py_minor > 6) or state.py3:
            response = muterun('pyh sys')
            self.assertEqual(response.exitcode, 0)
            self.assertTrue(len(response.stdout) > 0)
            self.assertEqual(response.stderr, b'')
        elif state.py_major == 2 and state.py_minor == 6:
            res = subprocess.check_call(['pyh', 'sys'])
            self.assertEqual(res, 0)

