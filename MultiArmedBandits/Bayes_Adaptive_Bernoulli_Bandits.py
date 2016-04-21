#!/bin/python
class BayesAdaptiveMDP:
    def __init__(self, num):
        self.alpha = [1.0 for i in xrange(num)];
        self.beta  = [1.0 for i in xrange(num)];
    def transform(self, idx, reward):
        if reward > 0:
            self.alpha[idx] += 1
        else:
            self.beta[idx]  += 1
    
 
