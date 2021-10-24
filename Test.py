from population import population 
from species import species
from genome import genome
from player import player
from history import connectionhistory
import miscFuncs
history = connectionhistory()
g = genome()
g.initalizeNetwork()
g.mutateConnection(history)
p = player(g)
#miscFuncs.drawNetwork(p.brain)

specie = species(p)


baby1 = specie.createChild(history)
baby2 = specie.createChild(history)

#miscFuncs.drawNetwork(baby2.brain)
specie.individer.append(baby1)
specie.individer.append(baby2)
#print(baby2.brain.nextnode)
#print(baby1.brain.nextnode)
miscFuncs.drawNetwork(baby1.brain)
miscFuncs.drawNetwork(baby2.brain)
baby3 = specie.createChild(history)
specie.individer.append(baby3)

for i in specie.individer:
    for c in i.brain.connections.values():
        pass
        #print(c.weight)
#for i in baby3.brain.nodes:
#    print(i.id)
#print(len(baby3.brain.connections))
miscFuncs.drawNetwork(baby3.brain)



