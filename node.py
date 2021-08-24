import numpy
import math
from connection import connection
class Node():
    def __init__(self, id, layer):
        self.id = id
        self.layer = layer
        self.inputsum = 0 #Detta kanske ska vara None
        self.activationvalue = 0
        self.outconnections = []


    def sigmoid(self):
        return 1/(1 + (math.exp(-self.inputsum)))

    def sendvalue(self, genome): 
        activationvalue = self.sigmoid()
        for connection in self.outconnections:  #Går igenom all utgående connections för denna noden och skicka ut activationvalue * vikt
            if connection.enabled: #Ifall den inte är enabled så skicka inte
                nodeid = connection.output
                weight = connection.weight
                node = genome.getNodeFromId(nodeid)
                node.inputsum += weight * activationvalue 
#1,7310