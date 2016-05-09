#/bin/python
import sys
sys.path.append("./secret")

from policy_value import *
import grid_mdp
import random
random.seed(0)
import numpy as np


def update_value(value, f, a, tvalue, alpha):
    pvalue        = value.qfunc(f, a);
    error         = pvalue - tvalue; 
    fea           = value.get_fea_vec(f, a);
    policy.theta -= alpha * error * fea;     

def update_softmaxpolicy(policy, f, a, qvalue, alpha):

    fea  = policy.get_fea_vec(f,a);
    prob = policy.pi(f);
    
    delte_logJ = fea;
    for i in xrange(len(policy.actions)):
        a1          = policy.actions[i];
        fea1        = policy.get_fea_vec(f,a1);
        delta_logJ -= fea1 * prob[i];

    policy.theta -= alpha * delta_logJ * qvalue; 

################ Different model free RL learning algorithms #####
def mc(grid, policy, num_iter1, alpha):
    actions = grid.actions;
    gamma   = grid.gamma;
    for i in xrange(len(policy.theta)):
        policy.theta[i] = 0.1

    for iter1 in xrange(num_iter1):

        f_sample = []
        a_sample = []
        r_sample = []   
        
        f = grid.start()
        t = False
        count = 0
        while False == t and count < 100:
            a = policy.take_action(f)
            t, f1, r  = grid.receive(a)
            f_sample.append(f)
            r_sample.append(r)
            a_sample.append(a)
            f = f1            
            count += 1


        g = 0.0
        for i in xrange(len(f_sample)-1, -1, -1):
            g *= gamma
            g += r_sample[i];
        
        for i in xrange(len(f_sample)):
            update_policy(policy, f_sample[i], a_sample[i], g, alpha)

            g -= r_sample[i];
            g /= gamma;
        

    return policy

def sarsa(grid, policy, value, num_iter1, alpha):
    actions = grid.actions;
    gamma   = grid.gamma;
    for i in xrange(len(policy.theta)):
        value.theta[i]  = 0.1
        policy.theta[i] = 0.0;

    for iter1 in xrange(num_iter1):
        f = grid.start();
        a = actions[int(random.random() * len(actions))]
        t = False
        count = 0

        while False == t and count < 100:
            t,f1,r      = grid.receive(a)
            a1          = policy.take_action(f1)
            update_value(value, f, a, r + gamma * value.qfunc(f1, a1), alpha);
            update_policy(policy, f, a, value.qfunc(f,a), alpha);

            f           = f1
            a           = a1
            count      += 1

    return policy, y;


