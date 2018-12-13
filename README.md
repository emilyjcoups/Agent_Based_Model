# Hero Agent Game
> Hero agents compete to eat the most of the plotted environment. Enemy agents work against them. 

### Summary 
__Hero agents move around 300 x 300 plot, eating the environment to gain speed and sharing food stores with agents in their neighbourhood.__ 

__Enemy agents compete to eat the environment and steal heroes' stores.__

__The first hero to reach a food store of 3000 wins.__

### Game logic
  * User requested to set the number of heroes and enemies (within the console)
  * Heroes and enemies are created from the same Agent class. Their starting coordinates (between 0 and 299) are generated randomly. 
  * Heroes and enemies move randomly and eat the environment. Their speed increases as their stores increase and reach certain thresholds. 
  * The distance is calculated between each pair of heroes, as well as between heroes and enemies:
      * If hero pairs are within same neighbourhood, the hero with the lower store steals the store advantage from the other hero's store. 
      * If an enemy enters a hero's neighbourhood, the enemy steals the hero's entire store 
  * The first hero to achieve a store of 3000 is the winner and the game ends 
  * When the game ends:
      1. The finishing environment data and is printed to the _end_environment.txt_ file
      2. The finishing positions and stores of each hero is printed to the _stores_records.txt_ file
      
### Installation

All libraries available within the [Anaconda](https://www.anaconda.com/download/) package. 

Please ensure IPython console backend is set to __automatic__.

### Contributions 
Contributions welcome. 

Please use [contributions](https://github.com/emilyjcoups/Agent_Based_Model/tree/contributions) branch.


### Meta 

Github: https://github.com/emilyjcoups

Twitter: [@emilycoupland](https://twitter.com/EmilyCoupland)

Website: https://emilycoupland.com/
