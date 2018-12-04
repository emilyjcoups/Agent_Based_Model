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

# Request input from user for number of heroes and enemies 
print("Welcome to the hero agent game. \nPlease set the number of hero and agents by inputting into the console below...")
num_heroes = int(input("Set the number of heroes: "))
num_enemies = int(input("Set the number of enemies: "))

# Declare variables 
heroes = []
enemies =[]
winners = []
environment = []
rowlist = []
# Declare figure for plot
fig = plt.figure(num= 1, figsize=(7, 5))
carry_on = True	

# Create 2D environment array from environment data file
f = open('environment.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) 

for row in reader:
    for value in row:
        rowlist.append(int(value))
    environment.append(rowlist)
    rowlist = []
f.close()

# Create agents and heroes (as many as inputted into console by user) and adds them to two separate lists 
for identity in range(num_heroes):
    heroes.append(agentframework.Agent(environment, heroes, (identity + 1), enemies))
    
for identity in range(num_enemies):
    enemies.append(agentframework.Agent(environment, heroes, (identity + 1), enemies))

# Set updates to the figure for animation 
def update(frame_number):

    fig.clear() # Clears existing markers and environment from the plot
    
    
    ax = fig.add_subplot(1,1,1) # Adds axes
    axes = plt.gca() # Gets axes
    # Sets ranges of axes
    axes.set_xlim([0,300]) 
    axes.set_ylim([0,300])
    # Adds environment and colour scale key
    plt.imshow(environment) 
    plt.colorbar(ax = axes, orientation= 'horizontal', extend = 'min', spacing = 'proportional', shrink = 0.5).set_label('Grass density')
    
    # Actions for heroes per iteration
    for hero in heroes:
        print(hero)
        global carry_on
        
        if hero.store >= 3000:
            winners.append(hero)
            plt.scatter(winners[0].x, winners[0].y, marker="D", c= "Orange")
            plt.text((winners[0].x + 25), (winners[0].y - 1), "{} is the winner!".format(winners[0].identity), fontsize=8, color='White', backgroundcolor='Black')
            print("We have a winner! Agent {} wins with a store of {}".format(winners[0].identity, winners[0].store))
            carry_on = False
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
            
        # for enemy in enemies:
        #    enemy.eat_neighbours(neighbourhood, hero)
        
        hero.move()
        hero.eat()
        hero.share_with_neighbours()
        # plt.text((enemy.x + 8), (enemy.y - 1), str(enemy.identity + 1), fontsize=8, color='White')
            
        enemy = mlines.Line2D([], [], color='Black', marker='x', linestyle='None', label='Enemy')
        key_slow = mlines.Line2D([], [], color='Grey', marker='o', linestyle='None', label='Slow hero')
        key_medium = mlines.Line2D([], [], color='Pink', marker='o', linestyle='None', label='Average hero')
        key_fast = mlines.Line2D([], [], color='Purple', marker='o', linestyle='None', label='Fast hero')
        
        plt.legend(handles=[key_slow, key_medium, key_fast, enemy], bbox_to_anchor=(1,1), bbox_transform=plt.gcf().transFigure, title='Agent key')

    for enemy in enemies:
        enemy.move()
        enemy.eat()
        plt.scatter(enemy.x, enemy.y, marker="x", c= 'Black')
        for hero in heroes: 
            enemy.eat_neighbours(hero)

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