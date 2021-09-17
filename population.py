#Hur många barn varje art ska ha fit (average fittness)/(average fitnessum (när det gäller alla arter)) * population size
import math
from species import species


class population():
    def __init__(self):
        self.species = []
        self.innoHistory = connectionhistory()
        self.players = []

    #Du behövder egentligen bara göra all evolution och sånt efter population i den nurvarande generationen har dött
    #Dela upp spelarna i art
    
    def putInSpecies(self):
        #ta bort alla individer i arten
        #Best kommer inte försvinna för den är en enskild variabel
        for art in self.species:
            self.individer = []
        #Gå igenom varje player och kolla om de är kompatibel med någon av arterna annars blir det en ny art
        for player in self.players:
            for art in self.species:
                if art.isCompatiable(player.brain):
                    art.individer.append(player)
                    break #Går till nästa player?
            #Ifall den kommer hit är den inte kompatibel med någon art så en ny måste skapas
            nyArt = species(player)
            self.species.append(nyArt)
    
    def sortSpecies(self): #Sorts species by fitness
        #Index 0 har bäst fitness
        self.species = sorted(self.species, key=lambda x: x.averageFit).reverse()
    
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
        self.species = filter(lambda x: not (len(x.individer) == 0), self.species)

    def killDroppedOffSpecies(self):
        self.species = filter(lambda x: not (x.dropOff == 15), self.species)

    def fitnessCalculation(self): #Göra fitnessharing här istället? Nej för då blir det anorlunda för antalet indivder här är större än vad det är senare
        #Räknar ut fitness från varje player
        #Nu ligger playersarna i arter så ugå inte från self.players
        for art in self.species:
            for individ in art.individer:
                pass #calculate the fitness
            art.sorteraArt
    def nextGeneration(self):
        self.putInSpecies()
        #Räkna ut fitness från varje player
        self.sortSpecies()
        self.killHalfSpecies()
        self.tommaSpecies()
        self.killDroppedOffSpecies()

        barn = []
        averageSum = self.averageFitnessSumma
        for art in self.species: #Du behöver ge innovationhistory
            barn.append(art.best)
            amountOfChildren = math.floor(art.averageFit/averageSum * self.size - 1) #mängden barn den arten får -1 för den bästa redan är i arten
            j = 0
            for i in range(0, amountOfChildren): #Inte plus 1 för 0 är 0 lmao
                barn.append(art.createChild(self.innoHistory))
        if len(barn) != self.size: #ifall det finns mer platser så ge mer barn till den bästa arten
            bestArt = self.species[0]
            antal = self.size - len(barn)
            for i in range(0,antal):
                barn.append(bestArt.createChild(self.innoHistory))
        self.individer = barn