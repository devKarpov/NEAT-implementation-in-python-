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
        if len(player.brain.connections) == 0:
            player.fitness = 1
            continue
        player.fitness = 1
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
            output = int(round(brain.useNetwork(input)[0]))
            if output == answer:
                player.correct += 1
        player.percent = player.correct/4
        if player.percent != 0.5:
            print(player.percent)
        if player.percent == 1:
            i = False
            miscFuncs.drawNetwork(player.brain)
    #print(gen)
    pop.nextGeneration()
    gen += 1

