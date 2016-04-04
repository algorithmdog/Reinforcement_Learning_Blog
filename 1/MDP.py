#/bin/python
import numpy;
import random;


class MDP:

    states         = [1,2,3,4,5,6,7,8] # 0 indicates end
    actions        = ['N','E','S','W']
    rewords        = dict();
    rewords['1_S'] = -1.0
    rewords['3_S'] = 1.0
    rewords['5_S'] = -1.0

    t              = dict();
    t['1_S']       = 6
    t['1_W']       = 1
    t['1_N']       = 1
    t['1_E']       = 2
    t['2_S']       = 2
    t['2_W']       = 1
    t['2_N']       = 2
    t['2_E']       = 3
    t['3_S']       = 7
    t['3_W']       = 2
    t['3_N']       = 3
    t['3_E']       = 4
    t['4_S']       = 4
    t['4_W']       = 3
    t['4_N']       = 4
    t['4_E']       = 5
    t['5_S']       = 8 
    t['5_W']       = 4
    t['5_N']       = 5
    t['5_E']       = 5

    def __init__(self, start_state == None):
        if None == start_state:
            self.current_state = int(ran.random() * 5) + 1
        else:
            self.current_state = start_state;

    def receive_action(self, action): ##return is_terminal,state, reward
        key = '%d_%s'%(self.current_state, action);
        if key in t: 
            self.current_state = t[key]; 


        is_terminal = False;
        if 6 == self.current_state or \
           7 == self.current_state or \
           8 == self.current_state:
            is_terminal = True;         

        if key not in rewards:
            r = -1.0;
        else:
            r = rewards[key];
           
        return is_terminal, self.current_state, r;


