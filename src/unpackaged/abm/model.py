# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import libraries
import matplotlib
import matplotlib.pyplot as plt
plt.ion()
import matplotlib.animation as animate
import random
import operator
import time
import agentframework
import csv


max_agents = 10
max_iterations = 10
neighbourhood = 20
agents = []
live_agents = [] 
environment = []
rowlist = []
point = []
plotted_agents =[]

# matplot variables 
fig = plt.figure(num= 1, figsize=(7, 7))
# ax = fig.add_axes([0, 0, 1, 1])
ax = fig.add_subplot(1,1,1)

# matplotlib.pyplot.ion()

# Creates agents (as many as max_agents value) with random coordinates (based on 100 x 100 grid) and adds them to list of agents
for j in range(max_agents):
    agents.append(agentframework.Agent(environment, agents))

def update(frame_number):
    
    fig.clear()
    ax = fig.add_subplot(1,1,1)
    axes = plt.gca()
    axes.set_xlim([0,100])
    axes.set_ylim([0,100])
    plt.imshow(environment)
    
    for i in range(max_agents):
        plt.scatter(agents[i].x, agents[i].y, c= None)
        agents[i].move()
        print(agents[i].x)
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)


        # restyle(graphDiv, update, [i]);
            
            # fig.clear()  

# Calculates distance between agents 

def distance_between(agents_row_a, agents_row_b):
    # print(agents_row_a.x, agents_row_b.x) 
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5 

# Read environment data 
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) 

for row in reader:
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.


# Plots agent locations

plt.ylim(0, 99)
plt.xlim(0, 99)
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False)
plt.show()

