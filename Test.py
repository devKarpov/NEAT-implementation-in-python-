from genome import genome
from node import Node
from connection import connection
from history import connectionhistory
import math
import miscFuncs
#kistory = connectionhistory()
genome1 = genome() #Kan du använda den här på flera och de syncar?
genome1.inputnodes = 1
genome1.initBiasNode()
genome1.initInputNodes()
genome1.initOutputNodes()
connection1 = connection(1, 2, 2)
connection2 = connection(0,2,1)
genome1.connections.append(connection1)
genome1.connections.append(connection2)
def orderGenes(genome):
    connections = genome.connections
    #Använd sorted
    sorted_cards = sorted(connections, key=lambda x: x.innovationnumber)
    for i in sorted_cards:
        print(i.innovationnumber)

##print(len(genome1.nodes[2].outconnections))

orderGenes(genome1)
miscFuncs.drawNetwork(genome1)
miscFuncs.printConnections(genome1)