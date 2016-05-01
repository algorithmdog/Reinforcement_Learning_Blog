#!/bin/python
import sys
import unittest

from evaluate import *

class eval_tester(unittest.TestCase):
    def test_eval(self):
        evaler = Evaler()
