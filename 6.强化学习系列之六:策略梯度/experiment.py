#!/bin/python
import sys
sys.path.append("./secret")
import random
random.seed(10)
import matplotlib.pyplot as plt
from gradient         import *
from policy_value     import *
from grid_mdp         import *
from evaluate         import *

if __name__ == "__main__":

    plt.figure(figsize=(12,6))


    grid            = Grid_Mdp();
    softmaxpolicy   = SoftmaxPolicy(grid, epsilon = 0.01);
    valuepolicy     = ValuePolicy(grid, epsilon = 0.01);
    evaler          = Evaler(grid);

    softmaxpolicy, y = sarsa(grid, evaler, softmaxpolicy, valuepolicy, 2000, 0.01)
    plt.plot(y, "-", label="sarsa");        
    

    plt.xlabel("number of iterations")
    plt.ylabel("square errors")
    plt.legend()
    plt.show();
