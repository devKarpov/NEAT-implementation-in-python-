#De som implementerar verkar bara låta lagret på en ny node vara = fromnode.layer + 1

Connectionhistory = None #Detta kommer vara globalt för alla nätverk senare.
class genome():
    def __init__(self):
        self.nextnode = 1
        self.nodes = [] #Biasnoden ska ha sitt värde = 0
        self.connections = [] #Alla connections som det nuvarande nätverket har i sina gener
        self.inputnodes = 2
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
            self.nextnode =+ 1

    def InitBiasNode(self): #Biasnode har värde = 0
        bias = Node(0, 1)
        self.biasnode = bias
    
    def initOutputNodes(self): #Känns som man borde kunna göra det här efter man har init gömda nodsen för att spara på prestanda, Körs egentligne
        for i in range(1, self.outputnodes + 1): #Sätter nextnode som värdet på varje output node och skapar nya nodes med layer = 2 eftersom det är output layer
            node = Node(self.nextnode, 2) #Skapar Node med nextnode som Id och lagret = 1
            self.nodes.append(node)
            self.nextnode =+ 1
    
    def getNodeFromId(self, id): #Säger säg självt
        return self.nodes[id]
#Fortsätt utifrån att du har connections och nodes(utan node.layer insatt)



    