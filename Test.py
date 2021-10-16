from population import population 

import miscFuncs
pop = population()

pop.startPopulation()
pop.nextGeneration()
for i in pop.players:
    miscFuncs.drawNetwork(i.brain)
