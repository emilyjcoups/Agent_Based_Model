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
    '''        
    @property
    def get_x(self):
        return self.x
    
    @property
    def set_x(self, value):
        self.x = value
        
    @property
    def get_y(self):
        return self.y
    
    @property
    def set_y(self, value):
        self.y = value
    ''' 
    
    
    def move(self):
        
        if self.store > 3000:
            
            if random.random() < 0.5:
                self.y = (self.y + 2) % 100
            else:
                self.y = (self.y - 2) % 100
        
            if random.random() < 0.5:
                self.x = (self.x + 2) % 100
            else:
                self.x = (self.x - 2) % 100
                
 
        elif self.store > 2000:
            
            if random.random() < 0.5:
                self.y = (self.y + 2) % 100
            else:
                self.y = (self.y - 2) % 100
        
            if random.random() < 0.5:
                self.x = (self.x + 2) % 100
            else:
                self.x = (self.x - 2) % 100
            
            
        else:
            
            if random.random() < 0.5:
                self.y = (self.y + 1) % 100
            else:
                self.y = (self.y - 1) % 100
        
            if random.random() < 0.5:
                self.x = (self.x + 1) % 100
            else:
                self.x = (self.x - 1) % 100
    
    def eat(self): 
        
        if self.environment[self.y][self.x] > 200:
            self.environment[self.y][self.x] -= 20
            self.store += 20
        elif self.environment[self.y][self.x] > 140:
            self.environment[self.y][self.x] -= 14
            self.store += 14
        elif self.environment[self.y][self.x] > 120:
            self.environment[self.y][self.x] -= 12
            self.store += 12
        elif self.environment[self.y][self.x] > 80:
            self.environment[self.y][self.x] -= 8
            self.store += 8
        else: 
            self.environment[self.y][self.x] -= 5
            self.store += 5
            
            

# elif self.environment[self.y][self.x] > 20:
#                self.environment[self.y][self.x] -= 20
#                self.store += 20
#            elif self.environment[self.y][self.x] > 10:
#                self.environment[self.y][self.x] -= 10
#                self.store += 10
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                if self.store > agent.store:
                    self.store -= agent.store
                    agent.store += self.store
                
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
            