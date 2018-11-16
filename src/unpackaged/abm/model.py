# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import libraries

import operator
import matplotlib.pyplot 
import time
import agentframework

# Calculates distance between agents 

def distance_between(agents_row_a, agents_row_b):
    # print(agents_row_a.x, agents_row_b.x) 
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5 

# Variable holding maximum number of agents 

max_agents = 10
max_iterations = 100

# List of agents
agents =[]

# Creates agents (as many as max_agents value) with random coordinates (based on 100 x 100 grid) and adds them to list of agents
for i in range(max_agents):
    agents.append(agentframework.Agent())
    # agents.append([random.randint(0, 100), random.randint(0, 100)])
    
# Moves each agent randomly 
for j in range(max_iterations):
    for i in range(max_agents):
        agents[i].move()

# print(agents)

''' Testing
a = agentframework.Agent()
print(a.y, a.x)

a.move()
print(a.y, a.x)
''' 

# Plots agent locations

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(max_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()


# Note to self: use agent in agents?
for k in range(max_agents): 
    for l in range(max_agents): 
        distance = distance_between(agents[l], agents[k])
        # print (distance)
