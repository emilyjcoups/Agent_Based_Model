# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import libraries

import random
import operator
import matplotlib.pyplot 

# Variable holding maximum number of agents 

max_agents = 10
max_iterations = 100

# List of agents
agents =[]

# Creates agents (as many as max_agents value) with random coordinates (based on 100 x 100 grid) and adds them to list of agents
for i in range(max_agents):
    agents.append([random.randint(0, 100), random.randint(0, 100)])
    
# Moves each agent randomly 
for i in range(max_iterations):
    for i in range(max_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
            
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


print(agents)

''' Calculate Euclidian distance between agents 
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5 

print(answer)
'''

# Plots agent locations

matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range(max_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
'''
eastern_agent = (max(agents, key= operator.itemgetter(1)))
matplotlib.pyplot.scatter(eastern_agent[1], eastern_agent[0], color='red')
'''
matplotlib.pyplot.show()

# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.