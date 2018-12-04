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

# DECLARE FUNCTIONS

# Keeps animation running as long as carry_on = true 
def gen_function():
    global carry_on
    a = 0
    while carry_on:
        yield a
        a = a + 1
        
# Writes end environment to file end_environment.txt 
def end_game():
    print('End game function called')
    with open('end_environment.txt', 'w') as e:
        e.write("END ENVIRONMENT: \n")
        for row in environment: 
            e.write(" ".join(str(value) for value in row) +"\n")
        e.write("DOCUMENT END \n")
        e.close()
        
    with open('stores_record.txt', 'a') as s:
        s.write("GAME STARTS with {} heroes and {} enemies: \n".format(num_heroes, num_enemies))
        for hero in heroes:
            s.write("Hero {} finishes with a total store of {}. \n".format(hero.identity, hero.store))
        s.write("GAME ENDS \n")
        s.close()
        
# Sets updates to figure per iteration 
def update(frame_number):

    # Creates figures and axes:
    fig.clear() # Clears figure so that updated markers and environment can be applied at each iteration 
    axes = plt.gca() # Points to axis
    # Sets ranges of axes:
    axes.set_xlim([0,300]) 
    axes.set_ylim([0,300])
    # Adds environment and colour scale key:
    plt.imshow(environment) 
    plt.colorbar(ax = axes, orientation= 'horizontal', extend = 'min', spacing = 'proportional', shrink = 0.5).set_label('Environment density')
    
    # Plots and actions for heroes:
    
    for hero in heroes: # Loops through heroes 
        print(hero) # Heroes prints location and store to console 
        global carry_on # Access to stopping condition variable 
        
        
        # Plots heroes according to status:
        
        if hero.store >= 3000: # First hero to reach store of 3000 wins and is plotted as winner
            winners.append(hero)
            plt.scatter(winners[0].x, winners[0].y, marker="D", c= "Orange")
            plt.text((winners[0].x + 25), (winners[0].y - 1), "{} is the winner!".format(winners[0].identity), fontsize=8, color='White', backgroundcolor='Black')
            print("We have a winner! Hero {} wins with a store of {}".format(winners[0].identity, winners[0].store) + "\n Remaining heroes:" )
            carry_on = False
            end_game()
            
        elif hero.store >= 2500: # Fast heroes plotted
            plt.scatter(hero.x, hero.y, c= 'Purple', label='Fast')
            plt.text((hero.x + 8), (hero.y - 1), str(hero.identity), fontsize=8, color='White')
        elif hero.store >= 1000: # Medium heroes plotted
            plt.scatter(hero.x, hero.y, c= 'Pink', label= 'Average')
            plt.text((hero.x + 8), (hero.y - 1), str(hero.identity), fontsize=8, color='White')
        elif hero.store < 1000: # Fast heroes plotted
            plt.scatter(hero.x, hero.y, c= 'Grey', label= 'Slow')
            plt.text((hero.x + 8), (hero.y - 1), str(hero.identity), fontsize=8, color='White')
        
        # Actions for heroes (movement and sharing and eating of environment)
        hero.move()
        hero.eat()
        hero.share_with_neighbours()
        
        # Creates key for hero markers
        enemy = mlines.Line2D([], [], color='Black', marker='x', linestyle='None', label='Enemy')
        key_slow = mlines.Line2D([], [], color='Grey', marker='o', linestyle='None', label='Slow hero')
        key_medium = mlines.Line2D([], [], color='Pink', marker='o', linestyle='None', label='Average hero')
        key_fast = mlines.Line2D([], [], color='Purple', marker='o', linestyle='None', label='Fast hero')
        plt.legend(handles=[key_slow, key_medium, key_fast, enemy], bbox_to_anchor=(1,1), bbox_transform=plt.gcf().transFigure, title='Agent key')

    # Plots and actions for enemies 
    for enemy in enemies:
        enemy.move()
        enemy.eat() 
        plt.scatter(enemy.x, enemy.y, marker="x", c= 'Black')
        for hero in heroes: 
            enemy.eat_neighbours(hero) # enemy eats neighbouring hereos' stores 
        

# Creates environment array from data file 
f = open('environment.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) 

for row in reader:
    for value in row:
        rowlist.append(int(value))
    environment.append(rowlist)
    rowlist = []
f.close()

# Creates heroes (as many as inputted into console by user) and adds them to hereos list
for identity in range(num_heroes):
    heroes.append(agentframework.Agent(environment, heroes, (identity + 1), enemies))
    
# Creates enemies (as many as inputted into console by user) and adds them to enemies list
for identity in range(num_enemies):
    enemies.append(agentframework.Agent(environment, heroes, (identity + 1), enemies))

# Animates plot 
animation = animate.FuncAnimation(fig, update, interval=1, frames=gen_function, repeat=False,)