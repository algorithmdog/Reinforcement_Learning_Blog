#!/bin/python
import math  as ma;
import numpy as np;
from policy   import *;
from grid_mdp import *;

class Trajectory:
    def __init__(self):
        ## len(states) = len(actons) + 1
        ## s_0,a_0,s_1,a_1,...,s_n,a_n,s_end
        self.states  = [];
        self.actions = [];

def gen_trajectories(mdp, policy, num):
        trajectories = [];
        gamma  = mdp.getGamma();

        for iter1 in xrange(num):
            trajectory = Trajectory();             
            s  = mdp.start();
            trajectory.states.append(s);            

            t    = False;
            num  = 0;
            coef = 1; 
            while False == t and num < 100:      
                num    += 1;

                actions = [];
                prob    = [];
                for a in mdp.actions:
                    actions.append(a); 
                    prob.append(policy.pi(s,a));

                a = actions[len(actions)-1];
                p = ra.random();
                sum1 = 0.0;
                for i in xrange(len(actions)):
                    sum1 += prob[i];
                    if sum1 >= p:   
                        a = actions[i];
                        break;


                t,s,_ = mdp.receive(a);
                coef *= gamma;

                trajectory.states.append(s);
                trajectory.actions.append(a);
        
            trajectories.append(trajectory);

        return trajectories;


