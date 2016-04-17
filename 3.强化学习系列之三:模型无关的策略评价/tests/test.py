#!/bin/python
import unittest

from model_free_policy_evaluation import *

class test(unittest.TestCase):

    def test_td(self):
        s = [[1,2,3],[4,3]]
        a = [['e','e','s'],['w','s']]
        r = [[0,0,1],[0,1]]

        vfunc = td(0.5,0.5,s,a,r)
        print vfunc


