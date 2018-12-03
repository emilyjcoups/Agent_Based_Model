#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 13:26:36 2018
@author: emilycoupland
"""

import random
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, environment, agents, number, enemies):
        self.x = random.randint(0,299)
        self.y = random.randint(0,299)
        self.environment = environment
        self.neighbourhood = 30
        self.store = 0
        self.agents = agents
        self.enemies = enemies
        self.identity = number
       
    def __str__(self):
        return 'Agent {} says "My location is x {}, y {} and I have eaten {} worth of environment, yum!"'.format(self.identity, self.x, self.y, self.store)   

    def move(self):
        
        if self.store > 3000:
            
            if random.random() < 0.5:
                self.y = (self.y + 6) % 300
            else:
                self.y = (self.y - 6) % 300
        
            if random.random() < 0.5:
                self.x = (self.x + 6) % 300
            else:
                self.x = (self.x - 6) % 300
                
 
        elif self.store > 2000:
            
            if random.random() < 0.5:
                self.y = (self.y + 4) % 300
            else:
                self.y = (self.y - 4) % 300
        
            if random.random() < 0.5:
                self.x = (self.x + 4) % 300
            else:
                self.x = (self.x - 4) % 300
            
            
        else:
            
            if random.random() < 0.5:
                self.y = (self.y + 2) % 300
            else:
                self.y = (self.y - 2) % 300
        
            if random.random() < 0.5:
                self.x = (self.x + 2) % 300
            else:
                self.x = (self.x - 2) % 300
    
    def eat(self): 
        
        if self.environment[self.y][self.x] > 250:
            self.environment[self.y][self.x] -= 25
            self.store += 20
        elif self.environment[self.y][self.x] > 100:
            self.environment[self.y][self.x] -= 20
            self.store += 14
        elif self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 8
        else: 
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]
            self.store += self.environment[self.y][self.x]
            
# avoid comparing itself 
    def share_with_neighbours(self):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= self.neighbourhood:
                if self.store > agent.store:
                    difference = self.store - agent.store
                    self.store -= difference
                    agent.store += difference
                
    def eat_neighbours(self, agent):
        distance = self.distance_between(agent)
        if distance <= self.neighbourhood - 20: 
            agent.store -= agent.store
            self.store += agent.store
            print("Agent {} store stolen by enemy".format(agent.identity))
        
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
            