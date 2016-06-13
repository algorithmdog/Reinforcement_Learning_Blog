#!/bin/python
import random
random.seed(0)
import numpy as np


def update(policy, s_fea, a, tvalue, alpha):
    pvalue        = policy.qfunc(s_fea, a);
    error         = pvalue - tvalue;
#    print "error"
#    print error;
#    print "before theta", policy.theta
#    print policy.theta 
    s_a_fea       = policy.get_state_action_fea(s_fea, a);
    policy.theta -= alpha * error * s_a_fea;
#    print "s_a_fea",s_a_fea     
#    print "after theta", policy.theta
#    print ""

################ Different model free RL learning algorithms #####
def sarsa(env, policy, num_iter1, alpha, gamma):
    for i in xrange(len(policy.theta)):
        policy.theta[i] = 0.1

    for iter1 in xrange(num_iter1):
        sum1      = 0.0
        s_f       = env.reset()
        a         = policy.epsilon_greedy(s_f)
        t         = False
        count     = 0

        while False == t and count < 10000:
            s_f1,r,t,i = env.step(a);
            a1         = policy.epsilon_greedy(s_f1)
            update(policy, \
                   s_f,\
                   a, \
                   r + gamma * policy.qfunc(s_f1, a1), \
                   alpha);

            s_f    = s_f1
            a      = a1
            count += 1

    return policy

def qlearning(env, policy, num_iter1, alpha, gamma):
    actions = policy.actions
    for i in xrange(len(policy.theta)):
        policy.theta[i] = 0.1

    for iter1 in xrange(num_iter1):
        s_f       = env.reset()
        a         = policy.epsilon_greedy(s_f)
        count     = 0
        t         = False

        while False == t and count < 10000:
            s_f1,r,t,i = env.step(a)
            qmax = policy.qfunc(s_f1,a) #random
            for a1 in policy.actions:
                pvalue = policy.qfunc(s_f1, a1);
                if qmax < pvalue:
                    qmax = pvalue;
            update(policy, s_f, a, r + gamma * qmax, alpha);

            s_f     = s_f1
            a       = policy.epsilon_greedy(s_f)
            count   += 1 
  
        if iter1%100 == 0:
            print "complete the %d epoches"%(iter1)

    return policy;

