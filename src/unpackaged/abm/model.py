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


max_agents = 10 # rename these > not max, descriptive 
max_iterations = 10
neighbourhood = 30
max_enemies = 10
heroes = []
enemies =[]
winners = []
environment = []
rowlist = []

# matplot variables 
fig = plt.figure(num= 1, figsize=(11, 5))
# ax = fig.add_axes([0, 0, 1, 1])
# ax = fig.add_subplot(1,1,1)

# Read environment data 
f = open('environment.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) 

# open('end_environment.txt', 'w').close()

for row in reader:
    for value in row:
        rowlist.append(int(value))
    environment.append(rowlist)
    rowlist = []
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.

# Rename agent hero 
# matplotlib.pyplot.ion()

# Creates agents (as many as max_agents value) with random coordinates (based on 100 x 100 grid) and adds them to list of agents
for identity in range(max_agents):
    heroes.append(agentframework.Agent(environment, heroes, (identity + 1), enemies))
    
for identity in range(max_agents):
    enemies.append(agentframework.Agent(environment, heroes, (identity + 1), enemies))

carry_on = True	

def update(frame_number):
    
    fig.clear()
    
    ax = fig.add_subplot(1,1,1)
    axes = plt.gca()
    axes.set_xlim([0,300])
    axes.set_ylim([0,300])
    plt.imshow(environment) 
    plt.colorbar()

    for enemy in enemies: 
        enemy.move()
        enemy.eat()
        plt.scatter(enemy.x, enemy.y, marker="x", c= 'Black')
    
    for hero in heroes:
        print(hero)
        global carry_on
        # need slow, fast and medium moving lists
        
        if hero.store >= 3000:
            carry_on = False
            winners.append(hero)
            print(winners)
            print(winners[0].y, winners[0].x)
            # end_game()
            '''
            with open('stores_record.txt', 'a+') as s:
                s.write("\n START GAME \n")
                for hero in heroes:
                    s.write("Agent {} finishes with a store of {}. \n".format(str(hero.identity), str(hero.store)))
                s.write("END GAME \n")
                s.close()
            '''

            plt.scatter(winners[0].x, winners[0].y, marker="D", c= "Orange")
            plt.text((winners[0].x + 10), (winners[0].y - 1), "{} is the winner!".format(winners[0].identity), fontsize=8, color='White', backgroundcolor='Black')
            print("We have a winner! Agent {} wins with a store of {}".format(winners[0].identity, winners[0].store))
                # end_game()
            
        elif hero.store >= 2500:
            plt.scatter(hero.x, hero.y, c= 'Purple', label='Fast')
            plt.text((hero.x + 8), (hero.y - 1), str(hero.identity), fontsize=8, color='White')
        elif hero.store >= 1000:
            plt.scatter(hero.x, hero.y, c= 'Pink', label= 'Average')
            plt.text((hero.x + 8), (hero.y - 1), str(hero.identity), fontsize=8, color='White')
        elif hero.store < 1000:
            plt.scatter(hero.x, hero.y, c= 'Grey', label= 'Slow')
            plt.text((hero.x + 8), (hero.y - 1), str(hero.identity), fontsize=8, color='White')
            
        for enemy in enemies:
            enemy.eat_neighbours(neighbourhood, hero)
        
        hero.move()
        hero.eat()
        hero.share_with_neighbours(neighbourhood)
        # plt.text((enemy.x + 8), (enemy.y - 1), str(enemy.identity + 1), fontsize=8, color='White')
            
        enemy = mlines.Line2D([], [], color='Black', marker='x', linestyle='None', label='Enemy')
        key_slow = mlines.Line2D([], [], color='Grey', marker='o', linestyle='None', label='Slow hero')
        key_medium = mlines.Line2D([], [], color='Pink', marker='o', linestyle='None', label='Average hero')
        key_fast = mlines.Line2D([], [], color='Purple', marker='o', linestyle='None', label='Fast hero')
        
        plt.legend(handles=[key_slow, key_medium, key_fast, enemy], bbox_to_anchor=(1,1), bbox_transform=plt.gcf().transFigure, title='Agent key')


#bbox trans bbox_transform=plt.gcf().transFigure 
        
def gen_function():
    global carry_on
    a = 0
    while carry_on:
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

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, frames=gen_function, repeat=False,)
plt.show()