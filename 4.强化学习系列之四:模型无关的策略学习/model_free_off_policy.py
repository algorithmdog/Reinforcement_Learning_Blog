#!/bin/python
import sys
sys.path.append("./secret")
import grid_mdp
import random

grid     = grid_mdp.Grid_Mdp(); 
states   = grid.getStates();
actions  = grid.getActions(); 
gamma    = grid.getGamma();
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
    pro[amax] += 1 - epsilon
    for i in xrange(len(actions)):
        pro[i] += epsilon / len(actions)

    ##choose
    r = random.random()
    s = 0.0
    for i in xrange(len(actions)):
        s += pro[i]
        if s >= r: return actions[i]
    return actions[len(actions)-1]



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

def qlearning_off_policy(alpha, state_sample, action_sample, reward_sample):
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
    print "qlearing_off_policy"    
    for s in states:
        for a in actions:
            print "%d_%s:%f"%(s,a,qfunc["%d_%s"%(s,a)])




if __name__ == "__main__":
    
    s, a, r = gensample()
    qlearning_off_policy(0.5, s, a, r)
