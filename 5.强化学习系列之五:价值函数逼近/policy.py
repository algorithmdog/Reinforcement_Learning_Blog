#!/bin/python
import sys
sys.path.append("./secret")

import grid_mdp
import random
random.seed(0)
import numpy as np


class Policy:
    def __init__(self, grid, epsilon):
        self.actions = grid.actions

        grid.start();
        t,hats,r = grid.receive(self.actions[0]);
        self.theta = [ 0.0  for i in xrange(len(hats)*len(self.actions)) ]
        self.theta = np.array(self.theta);
        self.theta = np.transpose(self.theta);
        
        self.epsilon = epsilon

    def get_fea_vec(self, fea, a):
        f = np.array([0.0 for i in xrange(len(self.theta))]);
            
        idx = 0
        for i in xrange(len(self.actions)):
            if a == self.actions[i]: idx = i;    
        for i in xrange(len(fea)):
            f[i + idx * len(fea)] = fea[i];
        
        return f

    def qfunc(self, fea, a):
        f = self.get_fea_vec(fea, a);
        return np.dot(f, self.theta);


    def epsilon_greedy(self, fea):
        ## max q action
        epsilon = self.epsilon;

        amax    = 0
        qmax    = self.qfunc(fea, self.actions[0]) 
        for i in xrange(len(self.actions)):
            a   = self.actions[i]
            q   = self.qfunc(fea, a)
            if qmax < q:
                qmax  = q;
                amax  = i; 
            
        ##probability
        pro = [0.0 for i in xrange(len(self.actions))]
        pro[amax] += 1- epsilon
        for i in xrange(len(self.actions)):
            pro[i] += epsilon / len(self.actions)

        ##choose
        r = random.random()
        s = 0.0
        for i in xrange(len(self.actions)):
            s += pro[i]
            if s >= r: return self.actions[i]
        
        return self.actions[len(self.actions)-1]
