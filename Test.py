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
connection1 = connection(1, 2, 1)
#connection2 = connection(0,2,1)
genome1.connections.append(connection1)
#genome1.connections.append(connection2)
genome1.mutateConnection()
genome1.makeReady()


##print(len(genome1.nodes[2].outconnections))
print(genome1.useNetwork({"1" : 100}))

miscFuncs.drawNetwork(genome1)
miscFuncs.printConnections(genome1)