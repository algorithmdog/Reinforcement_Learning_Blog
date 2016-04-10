#!/bin/python
import unittest

from policy_iteration import *

class policy_iteration_test(unittest.TestCase):

    def test_policy_evaluate(self):
        grid_mdp     = Grid_Mdp();
        policy_value = Policy_Value(grid_mdp)


        for i in policy_value.pi:
            policy_value.pi[i] = 's'
        policy_value.pi[2] = policy_value.pi[4] = 'e'

        policy_value.policy_evaluate(grid_mdp);

        self.assertTrue((policy_value.v[1] + 1.0) < 1e-6)
        self.assertTrue((policy_value.v[2] - 0.8) < 1e-6)
        self.assertTrue((policy_value.v[3] - 1.0) < 1e-6)
        self.assertTrue((policy_value.v[4] + 0.8) < 1e-6)
        self.assertTrue((policy_value.v[5] + 1.0) < 1e-6) 

    def test_policy_improve(self):
        grid_mdp     = Grid_Mdp()
        policy_value = Policy_Value(grid_mdp)

        for state in grid_mdp.states:
            if state in grid_mdp.terminal_states:   continue
            policy_value.v[state] = state
        policy_value.v[8] = 8

        policy_value.policy_improve(grid_mdp);
        for i in xrange(1,5):
            self.assertEqual(policy_value.pi[i], 'e')
        self.assertEqual(policy_value.pi[5], 's')
