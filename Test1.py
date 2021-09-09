from matplotlib import pyplot as plt
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

genome1.makeReady
for i in range(1,20):
    genome1.mutateConnection()
    genome1.mutateNode()
    genome1.makeReady

genome1.makeReady()
miscFuncs.drawNetwork(genome1)


#Dotsen vill vara så nära mitten som möjligt men ha samma distans på X

#mitten = monstNodes/2