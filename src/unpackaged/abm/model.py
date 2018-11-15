# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

# AGENT ONE

## Declare y and x variables 
    
y0, x0 = random.randint(0, 99), random.randint(0, 99)

## Change y and x based on random numbers (1/3)

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1


## Repeat change to y and x based on random numbers (2/3)

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1


## Repeat change to y and x based on random numbers (3/3)

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

# Check y0 and x0 values 
    
print(y0, x0)



# AGENT TWO

## Declare y and x variables 
    
y1, x1 = random.randint(0, 99), random.randint(0, 99)

## Change y and x based on random numbers (1/3)

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1


## Repeat change to y and x based on random numbers (2/3)

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1


## Repeat change to y and x based on random numbers (3/3)

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

# Check y1 and x1 values

print(y1, x1)

# Calculate Euclidian distance between agents 

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5 

print(answer)

# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.