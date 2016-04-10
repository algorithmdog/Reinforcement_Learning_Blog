#!/bin/python
import unittest

from value_iteration import *

class policy_iteration_test(unittest.TestCase):

    def test_policy_evaluation(self):
        grid_mdp     = Grid_Mdp();
        policy_value = Policy_Value(grid_mdp)

        policy_value.value_iteration(grid_mdp)

