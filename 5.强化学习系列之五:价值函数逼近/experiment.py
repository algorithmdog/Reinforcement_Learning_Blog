#!/bin/python
import sys
sys.path.append("./secret")
import random
random.seed(10)
import matplotlib.pyplot as plt
from model_free import *
from policy     import *
from evaluate   import *
from grid_mdp   import *

if __name__ == "__main__":

    plt.figure(figsize=(12,6))


    grid       = Grid_Mdp();
    policy     = Policy(grid, epsilon = 0.5);
    evaler     = Evaler(grid);
    grid_id    = Grid_Mdp_Id();
    policy_id  = Policy(grid_id, epsilon = 0.5);
    evaler_id  = Evaler(grid_id);

    #mc 
    policy, y = mc(grid, policy, evaler, num_iter1 = 10000, alpha = 0.01);
    plt.plot(y, "-", label="mc wall feature");        
    
    policy, y = mc(grid_id, policy_id, evaler_id, num_iter1 = 10000, alpha = 0.01);
    plt.plot(y, "-", label="mc id feature");
    
    #sarsa
    policy, y = sarsa(grid, policy, evaler, num_iter1 = 10000, alpha = 0.01);
    plt.plot(y, "--", label="sarsa wall feature");   
    
    policy, y = sarsa(grid_id, policy_id, evaler_id, num_iter1 = 10000, alpha = 0.01);
    plt.plot(y, "--", label="sarsa id feature");

    #qlearning
    policy, y = qlearning(grid, policy, evaler, num_iter1 = 10000, alpha = 0.01)
    plt.plot(y, "-.", label="qlearning wall feature");

    policy, y = qlearning(grid_id, policy_id, evaler_id, num_iter1 = 10000, alpha = 0.01)
    plt.plot(y, "-.", label="qlearning id feature");

    plt.xlabel("number of iterations")
    plt.ylabel("square errors")
    plt.legend()
    plt.show();
