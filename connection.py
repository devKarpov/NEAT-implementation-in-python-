import random
class connection():
    def __init__(self, input, output, innonr):
        self.input = input
        self.output = output
        self.weight = 1
        self.enabled = True
        self.innovationnumber = innonr
    #Testa det här https://stackoverflow.com/questions/31708478/how-to-evolve-weights-of-a-neural-network-in-neuroevolution
    #Frågan är hur man ska mutera vikterna
    #Vikterna ska vara mellan -1 och 1
    def mutate(self): #Med detta system kommer varenda vikt i ett nätverk gå igenom denna funktion. Det betyder att 
        randomInt = random.randint(0, 10)
        if randomInt <= 9: # 90% av tiden 
            randomfloat = round(random.uniform(0.5, 1.5),2 ) #Hur mycket ska man avrunda?

