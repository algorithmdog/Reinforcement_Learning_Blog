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

    ########## e-greedy vs greedy ######
    print "epsilon = 0.5"
    qfunc =  mc(num_iter1 = 5000, epsilon = 0.9)
    for s in states:
        for a in actions:
            key = "%d_%s"%(s,a)
            print "%d_%s:%f"%(s,a,qfunc[key])
    print "best"
    for s in states:
        for a in actions:
            key = "%d_%s"%(s,a)
            print "%d_%s:%f"%(s,a,best[key])
        


    plt.xlabel("number of iterations")
    plt.ylabel("square errors")
    plt.legend()
    plt.show();
