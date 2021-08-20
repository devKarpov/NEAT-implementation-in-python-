import numpy
import math
class Node():
    def __init__(self, id, layer):
        self.id = id
        self.layer = layer
        self.inputsum = 0
        self.activationvalue = 0
        self.outconnections = []


    def sigmoid(self):
        return 1/(1 + (math.exp((self.inputsum)* -1)))

