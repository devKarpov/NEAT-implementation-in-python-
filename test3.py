from matplotlib import pyplot as plt
from genome import genome
from node import Node
from connection import connection
from history import connectionhistory
import math
import miscFuncs
from population import population
import copy
pop = population()

pop.startPopulation()

pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()
pop.nextGeneration()

for i in pop.players:
    if len(i.brain.connections) != 0:
        #pass
        miscFuncs.drawNetwork(i.brain)