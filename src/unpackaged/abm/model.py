# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import libraries

import random
import operator
import matplotlib.pyplot 
import time

# Calculates distance between agents 

def distance_between(agents_row_a, agents_row_b):
    print(agents_row_a, agents_row_b) 
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5 

# Variable holding maximum number of agents 

max_agents = 10
max_iterations = 100

# List of agents
agents =[]

# Creates agents (as many as max_agents value) with random coordinates (based on 100 x 100 grid) and adds them to list of agents
for i in range(max_agents):
    agents.append([random.randint(0, 100), random.randint(0, 100)])
    
# Moves each agent randomly 
for j in range(max_iterations):
    for i in range(max_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
            
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


# print(agents)



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


# Calculate Euclidian distance between each pair of agents. 
# NOTE TO SELF: TIMER NEEDS UPDATED, DEPRECATED in PYTHON 3.3
            
start = time.clock()

# Note to self: use agent in agents?
for k in range(max_agents): 
    for l in range(max_agents): 
        distance = distance_between(agents[l], agents[k])
        print (distance)

end = time.clock()

print("time = " + str(end - start))