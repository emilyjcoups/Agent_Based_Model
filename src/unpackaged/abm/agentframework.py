#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 13:26:36 2018

@author: emilycoupland
"""

import random

class Agent:
    def __init__(self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        
# Future step - make x any y private and include set and get 
        
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
        
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
'''
    def __init__(self, environment):
        self.environment = environment
        self.store = 0
            '''
            
            