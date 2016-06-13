#!/bin/python
import math   as ma
import numpy  as np
import random as ra
import copy

class Policy:
    def pi(self, state, action):
        return 0;

class Optimal_Policy(Policy):
    
    def pi(self, state, action):
        m = dict();
        m['1_e'] = 1;
        m['2_e'] = 1;
        m['3_s'] = 1;
        m['4_w'] = 1;
        m['5_w'] = 1;
    
        key = "%s_%s"%(state, action);
        if key in m:
            return 1.0;
        else:
            return 0.0;

class Optimal_Epsilon_Policy(Policy):
    def __init__(self, epsilon = None):
        if None == epsilon:
            self.epsilon = 0.1;
        else:
            self.epsilon = epsilon;              

    def pi(self, state, action):
        m = dict();
        m['1_e'] = 1;
        m['2_e'] = 1;
        m['3_s'] = 1;
        m['4_w'] = 1;
        m['5_w'] = 1;
    
        key = "%s_%s"%(state, action);
        if key in m:
            return 1 - 3* self.epsilon;
        else:
            return self.epsilon;

class Apprenticeship_Policy(Policy):
    def __init__(self, mdp):
        self.states  = mdp.states;
        self.actions = mdp.actions; 
        self.q       = dict();
        for s in mdp.states:
            self.u  = np.array([ 0.0 for i in xrange(len(mdp.feas[s])) ]);
            break;
        for s in mdp.states:
            for a in mdp.actions:
                self.q["%s_%s"%(s,a)] = 0.0;
        
    def pi(self, state, action):
        max1 = -1000000000;
        for a in self.actions:
            v = self.q["%s_%s"%(state,a)];
            if max1 <  v:   max1 = v;

        q1 = ma.exp( self.q["%s_%s"%(state,action)] - max1 );
        s1 = 0.0;
        for a in self.actions:
            s1 += ma.exp( self.q["%s_%s"%(state, a)] - max1 );
        return q1 / s1;
    
    def compute_u(self, mdp):
        n      = 1000;
        gamma  = mdp.getGamma();
        self.u = np.array([ 0.0 for i in xrange(len(self.u)) ]);

        for iter1 in xrange(n):
            
            s  = mdp.start();
            u1 = copy.deepcopy(mdp.feas[s]);
            
            t    = False;
            num  = 0;
            coef = 1; 
            while False == t and num < 100:      
                num    += 1;

                actions = [];
                prob    = [];
                for a in mdp.actions:
                    actions.append(a); 
                    prob.append(self.pi(s,a));

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
                u1   += coef * mdp.feas[s];

            self.u += u1;

        self.u /= n;


class Maxent_Policy(Policy):
    def __init__(self, mdp):
        self.states  = mdp.states;
        self.actions = mdp.actions; 
        self.theta   = np.array([0.0 for i in xrange()]);

        
    def pi(self, state, action):
    

def evaluate(policy1, policy2, mdp):
    sum1 = 0
    for s in mdp.states:
        for a in mdp.actions:
            sum1 += ma.pow(policy1.pi(s,a) - policy2.pi(s,a),2)

    return sum1;
