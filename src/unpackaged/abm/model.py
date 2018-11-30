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
import matplotlib.lines as mlines
import random
import operator
import time
import agentframework
import csv


max_agents = 10
max_iterations = 10
neighbourhood = 7
agents = []
environment = []
rowlist = []
winners = []

# matplot variables 
fig = plt.figure(num= 1, figsize=(9, 5))
# ax = fig.add_axes([0, 0, 1, 1])
# ax = fig.add_subplot(1,1,1)

# Read environment data 
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) 

# open('end_environment.txt', 'w').close()

for row in reader:
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
    rowlist = []
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.


# matplotlib.pyplot.ion()

# Creates agents (as many as max_agents value) with random coordinates (based on 100 x 100 grid) and adds them to list of agents
for j in range(max_agents):
    agents.append(agentframework.Agent(environment, agents))

carry_on = True	

def update(frame_number):
    
    fig.clear()
    
    ax = fig.add_subplot(1,1,1)
    axes = plt.gca()
    axes.set_xlim([0,100])
    axes.set_ylim([0,100])
    plt.imshow(environment) 
    # include a scale and percentage of environment remaining 
    
# Reminder: before without multiple function calls for fuller agents, the agents jumped further but did not move more often and it took longer to have a winner 
    
    for i in range(max_agents):
        global carry_on
        print(agents[i].store)
        # need slow, fast and medium moving lists
        
        if agents[i].store >= 3000:
            winners.append(agents[i])
            # print(winners)
            carry_on = False
            
            with open('stores_record.txt', 'a+') as s:
                s.write("\n START GAME \n")
                for m in range(max_agents):
                    s.write("Agent {} finishes with a store of {}. \n".format(str(m+1), str(agents[m].store)))
                    print(agents[m].store)
                s.write("END GAME \n")
                s.close()
            
            if len(winners) == 1:
                plt.scatter(agents[i].x, agents[i].y, marker='D', c= "Orange")
                plt.text((agents[i].x + 4), (agents[i].y - 1), "{} is the winner!".format(i + 1), fontsize=8, color='White', backgroundcolor='Black')
                # end_game()
            elif len(winners) > 1:
                plt.scatter(agents[i].x, agents[i].y, marker='+', c= "Cyan")
                plt.text((agents[i].x + 4), (agents[i].y - 1), "{} is a runner up".format(i + 1), fontsize=8, color='White', backgroundcolor='Black')
            
            
        elif agents[i].store >= 2500:
            agents[i].move()
            agents[i].eat()
            plt.scatter(agents[i].x, agents[i].y, c= 'Purple', label='Fast')
            plt.text((agents[i].x + 2), (agents[i].y - 1), str(i + 1), fontsize=8, color='White')
        elif agents[i].store >= 1000:
            agents[i].move()
            plt.scatter(agents[i].x, agents[i].y, c= 'Pink', label= 'Average')
            plt.text((agents[i].x + 2), (agents[i].y - 1), str(i + 1), fontsize=8, color='White')
        elif agents[i].store < 1000:
            plt.scatter(agents[i].x, agents[i].y, c= 'Grey', label= 'Slow')
            plt.text((agents[i].x + 2), (agents[i].y - 1), str(i + 1), fontsize=8, color='White')
            
            
            # If two agents, work out the max
        # print(agents[i].x)
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
        key_slow = mlines.Line2D([], [], color='Grey', marker='o', linestyle='None', label='Slow')
        key_medium = mlines.Line2D([], [], color='Pink', marker='o', linestyle='None', label='Average')
        key_fast = mlines.Line2D([], [], color='Purple', marker='o', linestyle='None', label='Fast')
        plt.legend(handles=[key_slow, key_medium, key_fast], bbox_to_anchor=(1,1), bbox_transform=plt.gcf().transFigure, title='Agent speed')
    
#bbox trans bbox_transform=plt.gcf().transFigure 
        
def gen_function():
    global carry_on
    a = 0
    while ( a < 10000000000000000000000000000) & (carry_on):
        # print("a is equal to", a, "carry_on equals", carry_on)
        yield a
        a = a + 1
        
def end_game():
    print('End game function called')
    with open('end_environment.txt', 'w') as e:
        e.write("END ENVIRONMENT: \n")
        for row in environment: 
            e.write(" ".join(str(value) for value in row) +"\n")
        e.write("DOCUMENT END")
        e.close()
        
            
        


# Calculates distance between agents 

def distance_between(agents_row_a, agents_row_b):
    # print(agents_row_a.x, agents_row_b.x) 
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5 



    

# Plots agent locations

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, frames=gen_function, repeat=False,)
plt.show()