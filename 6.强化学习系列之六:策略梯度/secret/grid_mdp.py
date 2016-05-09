#/bin/python
import numpy as np
import random;

class Grid_Mdp_Id:

    def __init__(self, initial_state = None):

        self.states               = [1,2,3,4,5,6,7,8] 
        self.terminal_states      = dict()
        self.terminal_states[6]   = 1
        self.terminal_states[7]   = 1
        self.terminal_states[8]   = 1
        
        self.current_state        = 1
        if None == initial_state:
            self.current = int(random.random() * 5) + 1;
        else:
            if initial_state in self.terminal_states:
                raise Exception("initial_state(%d) is a terminal state"%\
                                (initial_state));
            self.current = initial_state;

        #feature of states
        self.feas    = dict();
        self.feas[1] = np.array([1,0,0,0,0,0,0,0]);
        self.feas[2] = np.array([0,1,0,0,0,0,0,0]);
        self.feas[3] = np.array([0,0,1,0,0,0,0,0]);
        self.feas[4] = np.array([0,0,0,1,0,0,0,0]);
        self.feas[5] = np.array([0,0,0,0,1,0,0,0]);        
        self.feas[6] = np.array([0,0,0,0,0,1,0,0]);
        self.feas[7] = np.array([0,0,0,0,0,0,1,0]);
        self.feas[8] = np.array([0,0,0,0,0,0,0,1]);

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

    def getGamma(self):
        return self.gamma;    

    def getActions(self):
        return self.actions

    def start(self, initial_state = None):

        self.current_state        = 1
        if None == initial_state:
            self.current = int(random.random() * 5) + 1;
        else:
            if initial_state in self.terminal_states:
                raise Exception("initial_state(%d) is a terminal state"%\
                                (initial_state));
            self.current = initial_state;

        return self.feas[self.current]

    def receive(self, action): ##return is_terminal,state, reward
        state = self.current;

        if state in self.terminal_states:
            return True, self.feas[state], 0

        key = '%d_%s'%(state, action);
        if key in self.t: 
            self.current = self.t[key]; 
        else:
            self.current = state;       

        is_terminal = False
        if self.current in self.terminal_states:
            is_terminal = True
      
        if key not in self.rewards:
            r = 0.0
        else:
            r = self.rewards[key];
           
        return is_terminal, self.feas[self.current], r;

class Grid_Mdp:

    def __init__(self, initial_state = None):

        self.states               = [1,2,3,4,5,6,7,8] 
        self.terminal_states      = dict()
        self.terminal_states[6]   = 1
        self.terminal_states[7]   = 1
        self.terminal_states[8]   = 1
        
        self.current_state        = 1
        if None == initial_state:
            self.current = int(random.random() * 5) + 1;
        else:
            if initial_state in self.terminal_states:
                raise Exception("initial_state(%d) is a terminal state"%\
                                (initial_state));
            self.current = initial_state;

        #feature of states
        self.feas    = dict();
        self.feas[1] = np.array([1,0,0,1]);
        self.feas[2] = np.array([1,0,1,0]);
        self.feas[3] = np.array([1,0,0,0]);
        self.feas[4] = np.array([1,0,1,0]);
        self.feas[5] = np.array([1,1,0,0]);        
        self.feas[6] = np.array([0,1,1,1]);
        self.feas[7] = np.array([0,1,1,1]);
        self.feas[8] = np.array([0,1,1,1]);

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

    def getGamma(self):
        return self.gamma;    

    def getActions(self):
        return self.actions

    def start(self, initial_state = None):

        self.current_state        = 1
        if None == initial_state:
            self.current = int(random.random() * 5) + 1;
        else:
            if initial_state in self.terminal_states:
                raise Exception("initial_state(%d) is a terminal state"%\
                                (initial_state));
            self.current = initial_state;

        return self.feas[self.current]

    def receive(self, action): ##return is_terminal,state, reward
        state = self.current;

        if state in self.terminal_states:
            return True, self.feas[state], 0

        key = '%d_%s'%(state, action);
        if key in self.t: 
            self.current = self.t[key]; 
        else:
            self.current = state;       

        is_terminal = False
        if self.current in self.terminal_states:
            is_terminal = True
      
        if key not in self.rewards:
            r = 0.0
        else:
            r = self.rewards[key];
           
        return is_terminal, self.feas[self.current], r;
