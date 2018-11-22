#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 13:26:36 2018

@author: emilycoupland
"""

import random
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, environment, agents):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agents = agents
        
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
    
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                average = self.store + agent.store
                self.store = average
                agent.store = average
                
                # print("sharing " + str(distance) + " " + str(average))
    
    def distance_between (self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
        

    # If distance is less than or equal to the neighbourhood
        # Sum self.store and agent.store .
        # Divide sum by two to calculate average.
        # self.store = average
            # agent.store = average
    # End if
# End loop
            