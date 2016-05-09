#!/bin/python
import unittest
import numpy as np

from model_free import *
from policy     import *; 

class qfunc_tester(unittest.TestCase):
    def test(self):
        policy = Policy();
        for i in xrange(len(policy.theta)):
            policy.theta[i] = 1.0;

        f  = np.array([1,1,1,1])
        a  = 'e'
        self.assertTrue(abs(policy.qfunc(f,a) - 4) < 0.0001);       
