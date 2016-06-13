#!/bin/python
import gym
import sys
import random
random.seed(0)
import numpy as np


class Policy:
    def __init__(self, env, epsilon):
        n_action     = env.action_space.n
        ##only support the (x,) shape
        shape        = env.observation_space.shape
        n_fea        = env.action_space.n * shape[0]
        self.actions = [ i    for i in xrange(n_action) ];
        self.theta   = [ 0.0  for i in xrange(n_fea) ]
        self.theta = np.array(self.theta);
        self.theta = np.transpose(self.theta);
        
        self.epsilon = epsilon

    def get_state_action_fea(self, state_fea, action):
        f = np.array([0.0 for i in xrange(len(self.theta))]);

        idx = 0
        for i in xrange(len(self.actions)):
            if action == self.actions[i]: 
                idx = i;
                break;    

        for i in xrange(len(state_fea)):
            f[i + idx * len(state_fea)] = state_fea[i];
        
        return f

    def qfunc(self, state_fea, action):
        f = self.get_state_action_fea(state_fea, action);
        return np.dot(f, self.theta);


    def greedy(self,fea):

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
        return amax

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
        pro[amax] += 1 - epsilon
        for i in xrange(len(self.actions)):
            pro[i] += epsilon / len(self.actions)

        ##choose
        r = random.random()
        s = 0.0
        for i in xrange(len(self.actions)):
            s += pro[i]
            if s >= r: return self.actions[i]
        
        return self.actions[len(self.actions)-1]
