import math
import genome
def drawNetwork(genome):
    layers = genome.layers
    nodesInLayers = []
    mostNodesInOneLayer = 0
    for layer in range(1,genome.layers + 1): 
        nodes = []
        for node in genome.nodes:
            if node.layer == layer:
                nodes.append(node.id)
        nodesInLayers.append(nodes)
        length = len(nodes)
        if length > mostNodesInOneLayer:
            mostNodesInOneLayer = length
    for layer in reversed(nodesInLayers): #Den börjar med det sista lagret
        antalNodes = len(layer)
        mellanrum = math.floor(mostNodesInOneLayer/antalNodes)
        string = ""
        t = 0
        for i in range(1, mostNodesInOneLayer + 1):
            if ((i/mellanrum) - int(i/mellanrum)) == 0:
                string += str(layer[t])
                t += 1
            else:
                string += "#"
        print(string)

def printConnections(genome):
    for connection in genome.connections:
        print(connection.input, "to", connection.output)