#!/bin/python

import random

class Bandits:
    def __init__(self, num):
        self.u = [random.random() for i in xrange(num)]
    def getReward(self, a):
        if a < 0 or a > len(self.u):
            raise Exception("Invalid a %d"%(a))

        r = random.random()
        if r <= self.u[a]:
            return 1;
        else:
            return 0;
            
        

