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


###############   Compute the gaps between current q and the best q ######
best = dict();
def read_best():
    f = open("best_qfunc")
    for line in f:
        line = line.strip()
        if len(line) == 0:  continue
        eles              = line.split(":")
        best[eles[0]] = float(eles[1])

def compute_error():
    sum1 = 0.0
    for key in qfunc:
        error = qfunc[key] - best[key]
        sum1 += error * error
    return sum1


##############   epsilon greedy policy #####
def epsilon_greedy(state, epsilon):
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



################ Different model free RL learning algorithms #####
def mc(epsilon):

    n = dict();
    for s in states:
        for a in actions:
            qfunc["%d_%s"%(s,a)] = 0.0
            n["%d_%s"%(s,a)] = 0.001

    for iter1 in xrange(1000):
        s_sample = []
        a_sample = []
        r_sample = []   
        
        s = states[int(random.random() * len(states))]
        t = False
        while False == t:
            a = epsilon_greedy(s, epsilon)
            t, s1, r  = grid.transform(s,a)
            s_sample.append(s)
            r_sample.append(r)
            a_sample.append(a)
            s = s1            

        g = 0.0
        for i in xrange(len(s_sample)-1, -1, -1):
            g *= gamma
            g += r_sample[i];
                
        for i in xrange(len(s_sample)):
            key = "%d_%s"%(s_sample[i], a_sample[i])
            n[key]      += 1.0;
            qfunc[key]   = (qfunc[key] * (n[key]-1) + g) / n[key]            
 
            g -= r_sample[i];
            g /= gamma;



    print ""
    print "mc"
    for s in states:
        for a in actions:
            print "%d_%s:%f"%(s,a,qfunc["%d_%s"%(s,a)]);


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
            a1          = epsilon_greedy(s1, epsilon)
            key1        = "%d_%s"%(s1,a1)
            qfunc[key]  = qfunc[key] + alpha * ( \
                          r + gamma * qfunc[key1] - qfunc[key])
            s           = s1
            a           = a1

    print ""
    print "sarsa"
    for s in states:
        for a in actions:
            print "%d_%s:%f"%(s,a,qfunc["%d_%s"%(s,a)])



def qlearning(alpha, epsilon):
   
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

            key1 = ""
            qmax = -1.0
            for a1 in actions:
                if qmax < qfunc["%d_%s"%(s1,a1)]:
                    qmax = qfunc["%d_%s"%(s1,a1)]
                    key1        = "%d_%s"%(s1,a1)
            qfunc[key]  = qfunc[key] + alpha * ( \
                          r + gamma * qfunc[key1] - qfunc[key])

            s           = s1
            a           = epsilon_greedy(s1, epsilon)


    print ""
    print "qlearning"
    for s in states:
        for a in actions:
            print "%d_%s:%f"%(s,a,qfunc["%d_%s"%(s,a)])


if __name__ == "__main__":
    read_best()
    

    mc(epsilon = 0.8);
    sarsa( 0.1, 0.8); 
    qlearning( 0.1, 0.8)
