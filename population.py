#Hur många barn varje art ska ha fit (average fittness)/(average fitnessum (när det gäller alla arter)) * population size
import copy
import math
import random
from species import species
from history import connectionhistory
from genome import genome
from player import player
import miscFuncs
import config
class population():
    def __init__(self):
        self.species = []
        self.innoHistory = connectionhistory()
        self.players = []
        self.size = config.populations["size"]
        self.dropoffrate = config.populations["stale"]
    #Du behövder egentligen bara göra all evolution och sånt efter population i den nurvarande generationen har dött
    #Dela upp spelarna i art
    
    def putInSpecies(self):
        #ta bort alla individer i arten
        #Best kommer inte försvinna för den är en enskild variabel
        #https://www.youtube.com/watch?v=cXVUSxSxY-E
        #Enligt den här video 
        for art in self.species:
            art.individer = []
        #Gå igenom varje player och kolla om de är kompatibel med någon av arterna annars blir det en ny art
        for player in self.players:
            i = False
            for art in self.species:
                if art.isCompatiable(player.brain):
                    art.individer.append(player)
                    i = True
                    break #Går till nästa player?
            if i:
                continue
            #Ifall den kommer hit är den inte kompatibel med någon art så en ny måste skapas
            nyArt = species(player)
            self.species.append(nyArt)
     
    ''' DET FUNKAR INTE
    def putInSpecies(self, list): #List med players
        
        #Ta random grabb från individer
        random.shuffle(list) #Gör så jag kan ta en random individ från players
        grabb = list[-1] #Tar den sista från shuffled listan (På grund av att pop går snabbare och tar bort den sista)
        nyArt = species(grabb)#Skapar ny art med den grabben som founder
        list.pop() #Tar bort den individen 
        marked = [] #players om inte ingick i arten
        #Gå igenom alla andra individer och se ifall dem är kompatibla med den arten. Om inte så markerar vi dem
        for player in list: #Går igenom resterande individer
            if nyArt.isCompatiable(player.brain):
                print("true")
                nyArt.individer.append(player)
            else:
                marked.append(player)
        self.species.append(nyArt)
        if len(marked) != 0: #Ifall det finns markerade
            #print(len(marked))
            self.putInSpecies(marked)
    '''

    def sortSpecies(self): #Sorts species by fitness
        self.species.sort(key=lambda x: (x.averageFit), reverse=True)

    def killHalfSpecies(self):
        for art in self.species:#T
            art.killHalf()
            art.sharedFitness() #Ska man göra detta förre eller efter man dödat av hälften?
            art.averageFitness()

    def averageFitnessSumma(self):
        sum = 0
        for art in self.species:
            sum += art.averageFit
        return sum
    
    def tommaSpecies(self):
        self.species = [x for x in self.species if not (len(x.individer) == 0)]

    def killDroppedOffSpecies(self):
        self.species = [x for x in self.species if not (x.dropOff == self.dropoffrate)]

    def killBadSpecies(self):
        sum = self.averageFitnessSumma()
        self.species = [x for x in self.species if not (x.averageFit/sum * self.size < 1)]

    def fitnessCalculation(self): #Göra fitnessharing här istället? Nej för då blir det anorlunda för antalet indivder här är större än vad det är senare
        #Räknar ut fitness från varje player
        #Nu ligger playersarna i arter så ugå inte från self.players
        '''for art in self.species:
            for individ in art.individer:
                individ.fitness = 1 + len(individ.brain.connections) * 100 + random.random()
            art.sorteraArt'''
        
        for art in self.species:
            '''for individ in art.individer:
                try:
                    if individ.correct > 3:
                        individ.fitness = individ.correct * 100
                except:
                    individ.fitness = random.random() + 1
            '''
            art.sorteraArt()

    def nextGeneration(self):
        self.putInSpecies()
        self.tommaSpecies()
        self.fitnessCalculation() 
        self.killHalfSpecies()
        #self.tommaSpecies() Här var den innan
        self.killDroppedOffSpecies()
        self.killBadSpecies()
        self.sortSpecies()
        for i in self.species:
            pass
            #print(i.averageFit)
        barn = []
        averageSum = self.averageFitnessSumma()
        for art in self.species: #Du behöver ge innovationhistory
            barn.append(copy.deepcopy(art.best))
            amountOfChildren = math.floor(art.averageFit/averageSum * self.size - 1) #mängden barn den arten får -1 för den bästa redan är i arten
            #print(amountOfChildren)
            j = 0
            for i in range(0, amountOfChildren): #Inte plus 1 för 0 är 0 lmao
                barn.append(art.createChild(self.innoHistory))
        if len(barn) != self.size: #ifall det finns mer platser så ge mer barn till den bästa arten
            bestArt = self.species[0]
            antal = self.size - len(barn)
            for i in range(0,antal):
                barn.append(bestArt.createChild(self.innoHistory))
        #print(len(self.species))
        #self.species = [] #Tar bort alla gamla arten
        self.players = barn
        #Här borde fitnessen clearas på alla indivder eftersom de bästa fortfarande har kvar sin fitness? 
        

    def startPopulation(self):
        
        for i in range(0,50):  #config?
            startBrain = genome()
            startBrain.initalizeNetwork()
            child = player(startBrain)
            child.brain.mutateConnection(self.innoHistory)
            self.players.append(child)