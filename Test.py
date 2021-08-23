from genome import genome
from node import Node
from connection import connection
from history import connectionhistory
import math
genome1 = genome()
genome1.inputnodes = 2
genome1.initBiasNode()
genome1.initInputNodes()
genome1.initOutputNodes()
connection1 = connection(1, 2)
connection2 = connection(0,2)
genome1.connections.append(connection1)
genome1.connections.append(connection2)
genome1.connectNodes()
#print(len(genome1.nodes[2].outconnections))
print(genome1.useNetwork({"1" : 100}))
