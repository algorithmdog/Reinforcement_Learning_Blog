#/bin/python
import unittest
from policy     import *
from grid_mdp   import *
from trajectory import *

class policy_test(unittest.TestCase):
    def test_evaluate(self):
        mdp               = Grid_Mdp();
        optimal_policy    = Optimal_Policy();
        apprentice_policy = Apprenticeship_Policy(mdp);
        print evaluate(optimal_policy, apprentice_policy, mdp); 
        print evaluate(optimal_policy, optimal_policy, mdp);
