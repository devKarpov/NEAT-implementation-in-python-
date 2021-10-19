from population import population 
from species import species
from genome import genome
from player import player
from history import connectionhistory
import miscFuncs
g = genome()
g.initalizeNetwork()
p = player(g)
history = connectionhistory()
specie = species(p)


baby1 = specie.createChild(history)
baby2 = specie.createChild(history)


specie.individer.append(baby1)
specie.individer.append(baby2)


baby3 = specie.createChild(history)
specie.individer.append(baby3)

for i in specie.individer:
    for c in i.brain.connections.values():
        print(c.weight)
miscFuncs.drawNetwork(baby3.brain)



