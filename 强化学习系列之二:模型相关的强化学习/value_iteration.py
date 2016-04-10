#/bin/python
import numpy;
import random;
from grid_mdp import Grid_Mdp

class Policy_Value:
    def __init__(self, grid_mdp):
        self.v  = [ 0.0 for i in xrange(len(grid_mdp.states) + 1)]
        
        self.pi = dict()
        for state in grid_mdp.states:
            if state in grid_mdp.terminal_states: continue

            self.pi[state] = grid_mdp.actions[ 0 ]
    
    def value_iteration(self, grid_mdp):
        for i in xrange(1000):
   
            delta = 0.0;
            for state in grid_mdp.states:
            
                    if state in grid_mdp.terminal_states: continue

                    a1      = grid_mdp.actions[0]
                    t, s, r = grid_mdp.transform( state, a1 )
                    v1      = r + grid_mdp.gamma * self.v[s]    

                    for action in grid_mdp.actions:
                        t, s, r = grid_mdp.transform( state, action )
                        if v1 < r + grid_mdp.gamma * self.v[s]:  
                            a1 = action
                            v1 = r + grid_mdp.gamma * self.v[s]                

                    delta         += abs(v1 - self.v[state])
                    self.pi[state] = a1
                    self.v[state]  = v1;
 
            if delta <  1e-6:
                break;       


if __name__ == "__main__":
        grid_mdp     = Grid_Mdp()
        policy_value = Policy_Value(grid_mdp)
        policy_value.value_iteration(grid_mdp)
        
        
        print "value:"
        for i in xrange(1,6):
            print "%d:%f\t"%(i,policy_value.v[i]),
        print ""
 
        print "policy:"
        for i in xrange(1,6):
            print "%d->%s\t"%(i,policy_value.pi[i]),
        print ""
