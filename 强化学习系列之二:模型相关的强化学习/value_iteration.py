#/bin/python
import numpy;
import random;

class Grid_Mdp:

    def __init__(self):

        self.states         = [1,2,3,4,5,6,7,8] # 0 indicates end
        self.terminal_states      = dict()
        self.terminal_states[6]   = 1
        self.terminal_states[7]   = 1
        self.terminal_states[8]   = 1

        self.actions        = ['n','e','s','w']

        self.rewards        = dict();
        self.rewards['1_s'] = -1.0
        self.rewards['3_s'] = 1.0
        self.rewards['5_s'] = -1.0

        self.t              = dict();
        self.t['1_s']       = 6
        self.t['1_e']       = 2
        self.t['2_w']       = 1
        self.t['2_e']       = 3
        self.t['3_s']       = 7
        self.t['3_w']       = 2
        self.t['3_e']       = 4
        self.t['4_w']       = 3
        self.t['4_e']       = 5
        self.t['5_s']       = 8 
        self.t['5_w']       = 4

        self.gamma          = 0.8

    def transform(self, state, action): ##return is_terminal,state, reward
        if state in self.terminal_states:
            return True, state, 0

        key = '%d_%s'%(state, action);
        if key in self.t: 
            next_state = self.t[key]; 
        else:
            next_state = state       
 
        is_terminal = False
        if next_state in self.terminal_states:
            is_terminal = True
      
        if key not in self.rewards:
            r = 0.0
        else:
            r = self.rewards[key];
           
        return is_terminal, next_state, r;

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
        
         

        print policy_value.pi
        print policy_value.v 
