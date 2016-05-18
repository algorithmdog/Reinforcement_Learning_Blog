#!/bin/python
import sys
sys.path.append("./secret");
from grid_mdp import *

###############  Compute the gaps between current q and the best q ######
class Evaler:
    def __init__(self, grid):
        self.grid = grid
        self.best = dict();
        f = open("./eval.data")
        for line in f:
            line = line.strip()
            if len(line) == 0:  continue
            eles  = line.split(":")
            self.best[eles[0]] = float(eles[1])
    

    def eval(self,  value_policy):
        grid = self.grid
        sum1 = 0.0
        for key in self.best:
            keys  = key.split("_")
            s     = int(keys[0])
            if s in grid.terminal_states:
                continue

            f     = grid.start(s)
            a     = keys[1]

            error = value_policy.qfunc(f,a) - self.best[key]
            sum1 += error * error

        return sum1


