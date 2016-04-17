#!/bin/python
import sys
sys.path.append("./secret")
import grid_mdp
import random

grid     = grid_mdp.Grid_Mdp(); 
states   = grid.getStates();
actions  = grid.getActions(); 
gamma    = grid.getGamma();
vfunc    = dict();
qfunc    = dict();


def greedy_pi_q(state, epsilon):
    ## max q action
    amax    = 0
    key     = "%d_%s"%(state, actions[0])
    qmax    = qfunc[key]

    for i in xrange(len(actions)):
        key = "%d_%s"%(state, actions[i])
        q   = qfunc[key]
        if qmax < q:
            qmax  = q;
            amax  = i; 
    
    ##probability
    pro = [0.0 for i in xrange(len(actions))]
    pro[amax] += epsilon
    for i in xrange(len(actions)):
        pro[i] += (1.0-epsilon) / len(actions)

    ##choose
    r = random.random()
    s = 0.0
    for i in xrange(len(actions)):
        s += pro[i]
        if s >= r: return actions[i]
    return actions[len(actions)-1]


def greedy_pi_v(state, epsilon):
    
    a      = actions[0]
    t,s,r  = grid.transform(state, a)
    action = 0
    vmax   = r + gamma * vfunc[s]  
    for i in xrange(len(actions)):
        a     = actions[i]
        t,s,r = grid.transform(state, a)      
        if vmax < r + gamma * vfunc[s]:
            action = i
            vmax   = r + gamma * vfunc[s]

    #the probability
    p = [0.0 for i in xrange(len(actions))]
    p[action] += epsilon;
    for i in xrange(len(actions)):
        p[i] += (1-epsilon)/(1.0 * len(actions))

    #random choice
    r = random.random()
    s = 0.0
    for i in xrange(len(actions)):
        s += p[i]
        if s >=  r: return actions[i];
    return actions[len(actions)-1]


def mc(epsilon):
   for s in states:
        vfunc[s] = 0.0 

def td_zero(alpha, epsilon):
    for s in states:
        vfunc[s] = 0.0
    
    for iter1 in xrange(1000):    
        state = states[int(random.random() * len(states))]
        t = False
        while False == t:
            action   = greedy_pi_v(state, epsilon) 
            t, s, r  = grid.transform(state, action)
            if True == t:  vfunc[s] = 0.0
            vfunc[state] = vfunc[state] + alpha * (r + gamma * vfunc[s] - vfunc[state])
            state    = s;                    

    print "td_zero"
    print vfunc

def sarsa(alpha, epsilon):
    for s in states:
        for a in actions:
            key = "%d_%s"%(s,a)
            qfunc[key] = 0.0

    for iter1 in xrange(1000):
        s = states[int(random.random() * len(states))]
        a = actions[int(random.random() * len(actions))]
        t = False
        while False == t:
            key         = "%d_%s"%(s,a)
            t,s1,r      = grid.transform(s,a)
            a1          = greedy_pi_q(s1, epsilon)
            key1        = "%d_%s"%(s1,a1)
            qfunc[key]  = qfunc[key] + alpha * ( \
                          r + gamma * qfunc[key1] - qfunc[key])
            s           = s1
            a           = a1

    print "sarsa"
    for s in states:
        for a in actions:
            print "%d_%s:%f"%(s,a,qfunc["%d_%s"%(s,a)])


def gensample():
    state_sample  = [];
    action_sample = [];
    reward_sample = []
    for i in xrange(1000):
        s_tmp = []
        a_tmp = []
        r_tmp = []

        s = states[int(random.random() * len(states))]
        t = False
        while False == t:
            a = actions[int(random.random() * len(actions))]
            t, s1, r  = grid.transform(s,a)
            s_tmp.append(s)
            r_tmp.append(r)
            a_tmp.append(a)
            s = s1            
        state_sample.append(s_tmp)
        reward_sample.append(r_tmp)
        action_sample.append(a_tmp)

    return state_sample, action_sample, reward_sample

def qlearning(alpha, state_sample, action_sample, reward_sample):
    for s in states:
        for a in actions:
            qfunc["%d_%s"%(s,a)] = 0.0
    
    for iter1 in xrange(len(state_sample)):
        for step in xrange(len(state_sample[iter1])):
            s = state_sample[iter1][step]
            a = action_sample[iter1][step]
            r = reward_sample[iter1][step]
            key = "%d_%s"%(s,a)
            
            qmax = 0.0            
            if len(state_sample[iter1]) - 1 > step:
                s1 = state_sample[iter1][step+1]
                key1    = "%d_%s"%(s1,actions[0])
                qmax    = qfunc[key1]
                for action in actions:
                    key1 = "%d_%s"%(s1,action)
                    q    = qfunc[key1]
                    if qmax < q:    qmax = q;                


            qfunc[key] += alpha *( r + gamma * qmax - qfunc[key])


    print ""
    print "qlearing"    
    for s in states:
        for a in actions:
            print "%d_%s:%f"%(s,a,qfunc["%d_%s"%(s,a)])


if __name__ == "__main__":
    td_zero(0.9, 0.99);
    sarsa(0.9, 0.99);
   
    s, a, r = gensample()
    qlearning(0.5, s, a, r)
