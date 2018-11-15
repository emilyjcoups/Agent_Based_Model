# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

# List of agents

agents =[]

# AGENT ONE

## Add random y and x coordinates (based on 100x100 grid) to list of agents

agents.append([random.randint(0, 99), random.randint(0, 99)])

## Change y and x based on random numbers (1/3)

print(agents)

if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1


## Repeat change to y and x based on random numbers (2/3)

if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1


## Repeat change to y and x based on random numbers (3/3)

if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

# Check y0 and x0 values 
    
print(agents)



# AGENT TWO

## Add random y and x coordinates (based on 100x100 grid) to list of agents

agents.append([random.randint(0, 99), random.randint(0, 99)])

## Change y and x based on random numbers (1/3)

print(agents)

if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1


## Repeat change to y and x based on random numbers (2/3)

if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1


## Repeat change to y and x based on random numbers (3/3)

if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

# Check y1 and x1 values

print(agents)

# Calculate Euclidian distance between agents 

answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5 

print(answer)

# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.