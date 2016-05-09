#!/bin/python
import unittest
import sys
sys.path.append("./secret")

from grid_mdp import *;

class grid_tester(unittest.TestCase):


    def test_init(self):
        grid = Grid_Mdp();
        d = dict();
        for i in xrange(1,6,1):
            d[i] = 1
        self.assertTrue(grid.current in d);
        
        grid = Grid_Mdp(1);
        self.assertEqual(grid.current, 1);
        t,f,r = grid.receive('n');
        self.assertFalse(t);
        fea = [1,0,0,1]
        for i in xrange(len(fea)):
            self.assertEqual(fea[i],f[i]);
        self.assertTrue((r-0.0) < 0.000001);
