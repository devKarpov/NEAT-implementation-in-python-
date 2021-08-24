#De som implementerar verkar bara låta lagret på en ny node vara = fromnode.layer + 1
from history import connectionhistory
from node import Node
from connection import connection
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

    def mutateConnection(self):
        #Pick random from node and to node
        if fromNode.layer == toNode.layer:
            pass
            #gör samma sak igen
        elif fromNode.layer > toNode.layer: #DETTA BETYDER ATT DET INTE FINNS RECURSIONS
            temporary = fromNode
            fromNode = toNode #Ifall fromnode kommer i ett lager efter toNode så blir fromNode = toNode
            toNode = temp
        innovationnumber = connectionhistory.IsNew(fromNode.id, toNode)
        newconnection = 