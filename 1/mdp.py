#/bin/python
import numpy;
import random;


class MDP:

    states         = [1,2,3,4,5,6,7,8] # 0 indicates end
    actions        = ['n','e','s','w']
    rewards        = dict();
    rewards['1_s'] = -1.0
    rewards['3_s'] = 1.0
    rewards['5_s'] = -1.0

    t              = dict();
    t['1_s']       = 6
    t['1_w']       = 1
    t['1_n']       = 1
    t['1_e']       = 2
    t['2_s']       = 2
    t['2_w']       = 1
    t['2_n']       = 2
    t['2_e']       = 3
    t['3_s']       = 7
    t['3_w']       = 2
    t['3_n']       = 3
    t['3_e']       = 4
    t['4_s']       = 4
    t['4_w']       = 3
    t['4_n']       = 4
    t['4_e']       = 5
    t['5_s']       = 8 
    t['5_w']       = 4
    t['5_n']       = 5
    t['5_e']       = 5

    def __init__(self, start_state = None):
        if None == start_state:
            self.current_state = int(ran.random() * 5) + 1
        else:
            self.current_state = start_state;

    def receive_action(self, action): ##return is_terminal,state, reward
        key = '%d_%s'%(self.current_state, action);
        if key in self.t: 
            self.current_state = self.t[key]; 


        is_terminal = False;
        if 6 == self.current_state or \
           7 == self.current_state or \
           8 == self.current_state:
            is_terminal = True;         

        if key not in self.rewards:
            r = 0.0
        else:
            r = self.rewards[key];
           
        return is_terminal, self.current_state, r;



            
