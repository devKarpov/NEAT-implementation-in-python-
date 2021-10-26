import random
from matplotlib import pyplot as plt
from genome import genome
from node import Node
from connection import connection
from history import connectionhistory
import math
import miscFuncs
from population import population
import copy
xor = [[0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]]


pop = population()

pop.startPopulation()
shuffled = random.sample(xor,4)
print(shuffled)
print(shuffled[0])

gen = 1
i = True
while i:
    shuffled = random.sample(xor,4)
    for player in pop.players:
        outputs = []
        player.fitness = 4
        player.correct = 0
        for bits in shuffled:
            bit1 = bits[0]
            bit2 = bits[1]
            answer = bits[2]
            input = {}
            input["1"] = bit1
            input["2"] = bit2
            brain = player.brain  
            brain.makeReady()
            output = brain.useNetwork(input)[0]
            outputs.append(output)
            #print(output)
        for i in range(0,4):
            #print(shuffled[i][2] - outputs[i])
            player.fitness -= (outputs[i] - shuffled[i][2]) ** 2
        print(player.fitness)
        if player.fitness > 3.4:
            
            input = {}
            input["1"] = 1
            input["2"] = 1
            output = brain.useNetwork(input)[0]
            print(output)
            print(gen)
            miscFuncs.drawNetwork(brain)
    pop.nextGeneration()
    gen += 1


#1−∑i(ei−ai)2 e expected | a acutal
