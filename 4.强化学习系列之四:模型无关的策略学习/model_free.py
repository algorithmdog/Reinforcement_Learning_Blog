#!/bin/python
import sys
sys.path.append("./secret")
import grid_mdp
import random
random.seed(10)
import matplotlib.pyplot as plt

grid     = grid_mdp.Grid_Mdp(); 
states   = grid.getStates();
actions  = grid.getActions(); 
gamma    = grid.getGamma();
qfunc    = dict();

###############   Compute the gaps between current q and the best q ######
best        = dict();

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
    pro[amax] += 1- epsilon
    for i in xrange(len(actions)):
        pro[i] += epsilon / len(actions)

    ##choose
    r = random.random()
    s = 0.0
    for i in xrange(len(actions)):
        s += pro[i]
        if s >= r: return actions[i]
    return actions[len(actions)-1]

################ Different model free RL learning algorithms #####

def mc(num_iter1, epsilon):


    x = []
    y = []

    n = dict();
    for s in states:
        for a in actions:
            qfunc["%d_%s"%(s,a)] = 0.0
            n["%d_%s"%(s,a)] = 0.001

    for iter1 in xrange(num_iter1):
        x.append(iter1);
        y.append(compute_error())

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

    plt.plot(x,y,"-",label="mc epsilon=%2.1f"%(epsilon));

def sarsa(num_iter1, alpha, epsilon):
    x = []
    y = []

    for s in states:
        for a in actions:
            key = "%d_%s"%(s,a)
            qfunc[key] = 0.0

    for iter1 in xrange(num_iter1):

        x.append(iter1)
        y.append(compute_error())

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

    plt.plot(x,y,"--",label="sarsa alpha=%2.1f epsilon=%2.1f"%(alpha,epsilon))


def qlearning(num_iter1, alpha, epsilon):
   
    for s in states:
        for a in actions:
            key = "%d_%s"%(s,a)
            qfunc[key] = 0.0
    x = []
    y = []


    for iter1 in xrange(num_iter1):
        x.append(iter1)
        y.append(compute_error())

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
   
    plt.plot(x,y,"-.,",label="q alpha=%2.1f epsilon=%2.1f"%(alpha,epsilon))



if __name__ == "__main__":
    read_best()
    plt.figure(figsize=(12,6))
    
    '''
    mc(num_iter1 = 50000, epsilon = 0.3);
    mc(num_iter1 = 50000, epsilon = 0.3);
    mc(num_iter1 = 50000, epsilon = 0.2);
    mc(num_iter1 = 50000, epsilon = 0.2);
    mc(num_iter1 = 50000, epsilon = 0.1);
    mc(num_iter1 = 50000, epsilon = 0.1);
    '''

    '''    
    sarsa(num_iter1 = 50000, alpha = 0.1,  epsilon = 0.3); 
    sarsa(num_iter1 = 50000, alpha = 0.1,  epsilon = 0.2);
    sarsa(num_iter1 = 50000, alpha = 0.1,  epsilon = 0.1);
    '''    

    '''
    sarsa(num_iter1 = 50000, alpha = 0.1,  epsilon = 0.2);
    sarsa(num_iter1 = 50000, alpha = 0.1,  epsilon = 0.2);
    sarsa(num_iter1 = 50000, alpha = 0.1,  epsilon = 0.2);
    '''

    '''    
    qlearning(num_iter1 = 5000, alpha = 0.1,  epsilon = 1)
    qlearning(num_iter1 = 5000, alpha = 0.1,  epsilon = 0.3);
    qlearning(num_iter1 = 5000, alpha = 0.1,  epsilon = 0.2);
    qlearning(num_iter1 = 5000, alpha = 0.1,  epsilon = 0.1);
    '''    

    '''
    qlearning(num_iter1 = 50000, alpha = 0.1,  epsilon = 0.2);
    qlearning(num_iter1 = 50000, alpha = 0.1,  epsilon = 0.2);
    '''

            
    mc(num_iter1 = 500, epsilon = 0.2)
    mc(num_iter1 = 500, epsilon = 0.1)
    sarsa(num_iter1 = 500, alpha = 0.2,  epsilon = 0.2);
    sarsa(num_iter1 = 500, alpha = 0.4,  epsilon = 0.2);
    sarsa(num_iter1 = 500, alpha = 0.2,  epsilon = 0.1);
    sarsa(num_iter1 = 500, alpha = 0.4,  epsilon = 0.1); 
    qlearning(num_iter1 = 500, alpha = 0.2,  epsilon = 0.2);
    qlearning(num_iter1 = 500, alpha = 0.4,  epsilon = 0.2);
    qlearning(num_iter1 = 500, alpha = 0.2,  epsilon = 0.1);
    qlearning(num_iter1 = 500, alpha = 0.4,  epsilon = 0.1);
    

    plt.xlabel("number of iterations")
    plt.ylabel("square errors")
    plt.legend()
    plt.show();
