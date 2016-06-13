import unittest
from policy     import *
from grid_mdp   import *
from trajectory import *

class trajectories_test(unittest.TestCase):
    def test_gen_trajectories(self):
        optimal_e_policy = Optimal_Epsilon_Policy(0.1);
        mdp              = Grid_Mdp();
        ts               = gen_trajectories(mdp, optimal_e_policy, 20);
        for i in xrange(20):
            print ts[i].states;
            print ts[i].actions;
        self.assertEquals(len(ts),20);
