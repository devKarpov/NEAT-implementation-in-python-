class connectionhistory():
    def __init__(self):
        self.innovations = [0] #Innovativa connections Anledningen till nollan är så att innovation numbers inte börjar på index 0 och så kan man returna 0 eventuellt
    
    
    def IsNew(self, input, output):
        for innoNr,connection in enumerate(self.innovations):
            if connection[0] == input and connection[1] == output: #Ifall detta är true finns det redan en sån connection i historian, Connection[0] är input etc
                return innoNr #get vilket innovation number
        self.innovations.append([input, output])
        return 0
    def getOutputconnections(nodeId): #

