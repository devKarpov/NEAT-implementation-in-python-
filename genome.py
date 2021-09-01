#De som implementerar verkar bara låta lagret på en ny node vara = fromnode.layer + 1
from history import connectionhistory
from node import Node
from connection import connection
import random
Connectionhistory = None #Detta kommer vara globalt för alla nätverk senare.

class genome():
    def __init__(self):
        self.nextnode = 1
        #Kanske borde använad en dictonary för nodsen, även för connections?
        self.nodes = [] #Biasnoden ska ha sitt värde = 0, Detta är i ordningen nodesen har kommit in i nätverket
        self.connections = [] #Alla connections som det nuvarande nätverket har i sina gener, Detta är i ordningen connections har kommit in i nätverket
        self.inputnodes = 1
        self.outputnodes = 1
        self.layers = 2
        self.biasnode = None
    
    def getOutputconnections(self, nodeId): #Ger alla enabled connections som en node ska skicka till
        connections = [] #Connections funktionen ska returna
        for connection in self.connections: #Går igenom nätverkets connections
            input = connection.input
            if input == nodeId:
                connections.append(connection)
        return connections #Kanske ska göra något om den är tom

    def initInputNodes(self):
        for i in range(1, self.inputnodes + 1): #Sätter i som värdet på varje input node och skapar nya nodes med layer = 1 eftersom det är input layer
            node = Node(self.nextnode, 1) #Skapar Node med nextnode som Id och lagret = 1
            self.nodes.append(node)
            self.nextnode += 1

    def initBiasNode(self): #Biasnode har värde = 0
        bias = Node(0, 1)
        bias.inputsum = 1
        self.nodes.append(bias)
        self.biasnode = bias
    
    def initOutputNodes(self): #Känns som man borde kunna göra det här efter man har init gömda nodsen för att spara på prestanda, Körs egentligne
        for i in range(1, self.outputnodes + 1): #Sätter nextnode som värdet på varje output node och skapar nya nodes med layer = 2 eftersom det är output layer
            node = Node(self.nextnode, 2) #Skapar Node med nextnode som Id och lagret = 1
            self.nodes.append(node)
            self.nextnode += 1
    
    def initalizeNetwork(self): #Behövs bara köras första gången nätverket går igång
        self.initBiasNode()
        self.initInputNodes()
        self.initOutputNodes()
    
    def getNodeFromId(self, id): #Säger säg självt
        return self.nodes[id]

    
    #Fortsätt utifrån att du har connections och nodes(utan node.layer insatt)

    def useNetwork(self, dict): #dictionaryn innehåller input till input nodsen
        #Gå ingenom alla inputnodes och ändra deras inputsum
        for i in range(1,self.inputnodes + 1):
            noden = self.getNodeFromId(i)
            value = dict[str(i)]
            noden.inputsum += value
        #Går igenom varje node i varje lager (börjar från input lager) och lägger på sin (activation value * weight) på alla outgoing connections i out nodens inputsum
        for layer in range(1,self.layers + 1): #Detta går också igenom output layer?
            for node in self.nodes:
                if node.layer == layer:
                    node.sendvalue(self)
        inputs = self.inputnodes
        return (self.getNodeFromId(inputs + 1).sigmoid())
    #KOLLA UPP LIST COMPREHENSIONS OCH LAMBDA

    def connectNodes(self): # Går igenom alla connections som genome har och ger de relevanta connectionsarna till nodsen.
        for connection in self.connections:
            if connection.enabled: #Ge bara om connectionen faktiskt är igång
                fromNode = connection.input
                fromNode = self.getNodeFromId(fromNode)
                fromNode.outconnections.append(connection)

    def clearNetwork(self): #Gör detta snabbare om det går
        for node in self.nodes:
            if node.id == 0: #Inte om bias node
                node.outconnections = [] #Fixa så biasnoden har activationvalue och inputsum som konstanter
                continue 
            node.activationvalue = None
            node.inputsum = 0 #Kanske ska vara None
            node.outconnections = []

    def makeReady(self):
        self.clearNetwork()
        self.connectNodes()

    def mutateConnection(self): #Detta är inte effektivt.
        #Hur kollar man så att det faktiskt går att göra en ny connection
        #Pick random from node and to node
        if fromNode.layer == toNode.layer:
            pass
            #gör samma sak igen
        elif fromNode.layer > toNode.layer: #DETTA BETYDER ATT DET INTE FINNS RECURSIONS
            temporary = fromNode
            fromNode = toNode #Ifall fromnode kommer i ett lager efter toNode så blir fromNode = toNode
            toNode = temp
        if self.connectionExists(fromNode.id, toNode.id):
            pass #Det betyder att en connection redan finns
        innovationnumber = connectionhistory.IsNew(fromNode.id, toNode.id)
        newconnection = connection(fromNode.id, toNode.id, innovationnumber) # Du måste sätta en random vikt på connectionen också
    
    def connectionExists(self, fromNodeId, toNodeId):
        for i in self.connections:
            if i.input == fromNodeId and i.output == toNodeId:
                return True
        return False

    def fullyConnected(self):
        for node in self.nodes:#Går igenom varje node
            layer = node.layer
            antalConnections = len(node.outconnections) #Får antalet connections den noden har just nu
            nodesEfter = 0
            for searchNode in self.nodes: #tar fram alla nodes efter noden, maximalet antal connections är antalet nodes efter den
                if searchNode.layer > layer:
                    nodesEfter += 1
            if antalConnections != nodesEfter: #Ifall dessa två nummer inte är desamma betyder det att nätverket inte är fullt
                return False
        return True

    def twoNodesToConnect(self): #Vad ifall det är en node med full connection
        randomNode = None
        layer = randomnode.layer
        possibleNodes = []
        for searchNode in self.nodes: #Går igenom alla nodesen
            if layer < searchNode.layer: #Om layer är lägre än search.layer är randomNode = fromNode vilket betyder att den får id1 för connectionExistsfunktionen
                id1 = randomNode.id
                id2 = searchNode.id
            elif layer < searchNode.layer: #Vice versa
                id1 = searchNode.id
                id2 = randomNode.id
            else: #Om de är i samma lager så gå bara till nästa node
                continue
            if not (self.connectionExists(id1, id2)): #Om connectionen inte existerar så lägg till NodeId i possible nodes
                possibleNodes.append(searchNode.id)
    
    def mutateNode(self):
        #Du måste få index för connectionen
        length = len(self.connections)
        i = random.randint(0, length-1) #få randomint
        randomConnection = self.connections[i]
        self.connections[i].Enabled = False #Måste den vara på från början för att det ska hända?

        fromNode = randomConnection.input
        toNode = randomConnection.output
        layer = fromNode.layer + 1
        if fromNode.layer + 1 == toNode.layer:
            for node in self.nodes:
                if node.layer > fromNode.layer:
                    node.layer += 1
        newNode = Node(self.nextnode, layer)
        self.nextnode += 1
        self.nodes.append(newNode)
        #Skapa de två nya connectionsarna
        Connectionhistory.isNew(fromNode.id, toNode.id)
        firstConnection = connection(fromNode.id, toNode.id)
        
        
        
        
                