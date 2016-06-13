#!/bin/python
import math   as ma;
import random as ra; 
import numpy  as np;
import matplotlib.pyplot as plt;
from policy     import *;
from grid_mdp   import *;
from trajectory import *;
from pulp       import *;
ra.seed(10);

class Apprenticeship_Learning:
    def __init__(self, mdp): 
        self.mdp          = mdp;
        for s in mdp.states:
            break;        
        self.theta        = np.array([ ra.random() for i in xrange(len(mdp.feas[s])) ]); 
        self.trajectories_u = np.array([ 0.0 for i in xrange(len(mdp.feas[s])) ]);

    def state_reward(self, state_fea):
        return np.dot(state_fea, self.theta);

    def compute_u(self, trajectories):
        for t in trajectories:
            coeff = 1;
            u     = np.array([ 0.0 for i in xrange(len(self.theta)) ]);
            for i in xrange(len(t.states)): 
                u       += coeff * mdp.feas[t.states[i]]; 
                coeff  *= mdp.gamma;
            self.trajectories_u += u;

        self.trajectories_u /= len(trajectories);

    def learn_policy(self, trajectories): 
        policy = Apprenticeship_Policy(self.mdp);
        n      = dict();
        for s_a in policy.q:
            n[s_a]        = 0.0001;
            policy.q[s_a] = 0.0;

        for t in trajectories:
            G = 0.0;   
            for i in xrange(len(t.states)-1,0,-1):
                s  = t.states[i];
                r  = self.state_reward(mdp.feas[s]);
                G *= self.mdp.gamma; 
                G += r; 
            for i in xrange(len(t.states)-1):
                s  = t.states[i];
                a  = t.actions[i];
                policy.q["%s_%s"%(s,a)] += G;
                n["%s_%s"%(s,a)]        += 1.0;
                G -= self.state_reward(mdp.feas[s]);
                G /= self.mdp.gamma;                  
 
                 
        for s_a in policy.q:
            if n[s_a] > 0.1:
                policy.q[s_a] /= n[s_a];

        return policy

    def guess_reward(self, policys):
        gamma = LpVariable("gamma");
        theta = [];
        for i in xrange(len(self.theta)):
            theta.append(LpVariable("theta_%d"%(i), -1.0,1.0));

        prob = LpProblem("guess_reward", LpMaximize);
        e = 0
        for i in xrange(len(self.theta)):
            e += theta[i]
        prob += e < 1
        prob += e > -1

        for p in policys:
            e = 0
            for u in xrange(len(self.trajectories_u)):
                e += theta[u] * self.trajectories_u[u]
                e -= theta[u] * p.u[u]
            e -= gamma
            prob += e >= 0
        prob += gamma;
        

        prob.solve()
        for i in xrange(len(self.theta)):
            self.theta[i] = value(theta[i])


    def learning(self, mdp, trajectories, epoches):        
        policys = [];
        policy0 = Apprenticeship_Policy(mdp);
        policy0.compute_u(mdp);
        policys.append(policy0);
        
        self.compute_u(trajectories);

        for iter1 in xrange(epoches):
            self.guess_reward(policys);
            policy = self.learn_policy(trajectories);
            policy.compute_u(mdp);
            policys.append(policy);


        return policys, self.theta;
        

if __name__ == "__main__":
    plt.figure(figsize=(12,6));
    y = [];
    
    mdp                    = Grid_Mdp(); 
    apprenticeship_policy  = Apprenticeship_Policy(mdp);
    learner                = Apprenticeship_Learning(mdp);   
    optimal_e_policy       = Optimal_Epsilon_Policy(0.05);
    trajectories           = gen_trajectories(mdp, optimal_e_policy, 5000);    

    policys, theta         = learner.learning(mdp, trajectories, epoches = 20);
    for i in xrange(len(policys)):
        differ =  evaluate(policys[i], optimal_e_policy, mdp);
        y.append(differ);
        print "iter %d: %f"%(i,differ);     
    for s in mdp.states:
        print "state %s reward %f"%(s,np.dot(theta,mdp.feas[s])); 

    plt.plot(y);
    plt.xlabel("number of iterations");
    plt.axis([0,20,0,5]);
    plt.legend();
    plt.show();
