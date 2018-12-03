# Hero Agent Game
> Hero agents compete to eat the most environment on a 300x300 graph plot.
### Summary 
__Hero agents move around 300 x 300 plot, eating the environment to gain speed and sharing food stores with agents in their neighbourhood. The first hero to reach a food store of 3000 wins. Enemy agents compete to eat the environment and steal heroes stores.__

### Game logic
  * Console requests user to enter values for the number of heroes and enemies in the game
  * Heroes and enemies are created from the same Agent class. Their locations based on random integers between 0 and 299.
  * Heroes and enemies move randomly eating environment. Their speed increases as their stores reach thresholds (num - num). 
  * Distance is calculated between each pair of heroes and between heroes and enemies:
      * If hero pairs are within same neighbourhood, the hero with the lower store steals the store advantage from the other hero's store. 
      * If an enemy shares a neighbourhood with a hero, the enemy steals the hero's entire store 
  * The first hero to achieve a store of 3000 is the winner and the game ends 
  * When the game ends:
      1. The finishing environment data and is printed to the _end_environment.txt_ file
      2. __The finishing positions and stores of each hero is printed to the --------- file
      
### Installation 
No installation requirements
