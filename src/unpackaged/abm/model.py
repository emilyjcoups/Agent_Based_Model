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
import csv

# Calculates distance between agents 

def distance_between(agents_row_a, agents_row_b):
    # print(agents_row_a.x, agents_row_b.x) 
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5 

environment = []
rowlist = []

f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)


for row in reader:
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.

# Variable holding maximum number of agents 

max_agents = 10
max_iterations = 100

# List of agents
agents =[]

# Creates agents (as many as max_agents value) with random coordinates (based on 100 x 100 grid) and adds them to list of agents
for i in range(max_agents):
    agents.append(agentframework.Agent(environment))
    # agents.append([random.randint(0, 100), random.randint(0, 100)])
    
# Moves each agent randomly 
for j in range(max_iterations):
    for i in range(max_agents):
        agents[i].move()
        agents[i].eat()
        
# print(agents)

# Plots agent locations

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(max_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()


# Note to self: use agent in agents?
for k in range(max_agents): 
    for l in range(max_agents): 
        distance = distance_between(agents[l], agents[k])
        # print (distance)
