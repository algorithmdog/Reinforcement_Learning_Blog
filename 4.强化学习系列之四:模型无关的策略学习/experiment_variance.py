#!/bin/python
import sys
sys.path.append("./secret")
import grid_mdp
import random
random.seed(0)
import matplotlib.pyplot as plt
from model_free import *


if __name__ == "__main__":
    read_best()
    plt.figure(figsize=(12,6))


    ############# variance ##################
    mc(num_iter1 = 6000, epsilon = 0.2);
    mc(num_iter1 = 6000, epsilon = 0.2);
    mc(num_iter1 = 6000, epsilon = 0.2);
    mc(num_iter1 = 6000, epsilon = 0.2);
    sarsa(num_iter1 = 6000, alpha = 0.2,  epsilon = 0.2);
    sarsa(num_iter1 = 6000, alpha = 0.2,  epsilon = 0.2);
    sarsa(num_iter1 = 6000, alpha = 0.2,  epsilon = 0.2);
    sarsa(num_iter1 = 6000, alpha = 0.2,  epsilon = 0.2);
    qlearning(num_iter1 = 6000, alpha = 0.2,  epsilon = 0.2);
    qlearning(num_iter1 = 6000, alpha = 0.2,  epsilon = 0.2);
    qlearning(num_iter1 = 6000, alpha = 0.2,  epsilon = 0.2);
    qlearning(num_iter1 = 6000, alpha = 0.2,  epsilon = 0.2);


    plt.xlabel("number of iterations")
    plt.ylabel("square errors")
    plt.legend()
    plt.show();
