#!/bin/python
import gym
def get_env(name):
    if 'Acrobot-v0' == name:
        return gym.make('Acrobot-v0')
    elif 'MountainCar-v0' == name:
        return gym.make('MountainCar-v0')
    elif 'CartPole-v0' == name:
        return gym.make('CartPole-v0')
    else:
        raise Exception('Not %s env found'%(name))

