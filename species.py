#ordera genesen från början så slipper du göra det flera gånger
import random
from genome import genome
from history import connectionhistory
from player import player
import numpy.random
class species():
    def __init__(self,best):
        self.best = best #Den bästa individen i artens genome
        self.individer = [best]
        self.averageFit = None
        self.dropOff = 0 #

    def averageFitness(self): #Dividebyzero
        totalfitness = 0
        for individ in self.individer:
            #print(individ.fitness)
            totalfitness += individ.fitness
        self.averageFit = totalfitness/(len(self.individer))
        #print(totalfitness)
    def sorteraArt(self): #Sorterar arten där högst fitness är först/ ökar också dropOff
        oldBest = self.best 
        sorted_species = sorted(self.individer, key=lambda x: x.fitness).reverse()        
        if sorted_species[0].fitness > self.best.fitness:
            self.best = sorted_species[0]
            if self.best.fitness <= oldBest.fitness:
                self.dropOff += 1
        self.individer = sorted_species
                
        
            
    def orderGenes(self, genes): #ger ordningen av generna där lägst innovationnumber går först, Gör till class variable
        #Varför behövs den här när gensen är i en dictionary?
        sorted_genes = sorted(genes, key=lambda x: x.innovationnumber)
        return sorted_genes
    
    def createArray(self, genes, n):
        #geneDict = {}
        #for connection in genes:
        #    nr = connection.innovationnumber
        #    geneDict[str(id)] = True
        #Nu bör genes redan från början vara en dictionary?
        array = []
        for i in range(0, n+1):#Ska det vara n+1?
            if str(i) in genes:
                array.append(1)
            else:
                array.append(0)
        return array
    #Engligt pappret ska du få alla disjoin genes totalt. Varesig de är från genome 1 eller 2.
    #Rent tekniskt så ifall du vet antalet excess genes borde du ganska lätt kunna räkna ut antalet disjoint genes
    #Code bullet satte coeffcienten för disjoint och excess som samma.
    #Vad ifall du gör de två generna till en matris. Där raderna är genome1 och 2 och kolumner representerar en gene. Om en kolumn är 0 1 så betyder det att det är en disjoint.
    #Sen måste du lösa
    #utgå från att genes är sorterade
    def findDisjoinGenes(self, genes1, genes2): 
        #vad ifall dem inte har några gener
        tgenes1 = self.orderGenes(genes1.values())
        tgenes2 = self.orderGenes(genes1.values())
        highest = 0
        lower = 0
        if len(tgenes1) == 0 and len(tgenes2) == 0:
            return 0,0
        elif len(tgenes1) == 0:
            highest = tgenes1[-1].innovationnumber
            lower = 0
        elif len(tgenes2) == 0:
            highest = tgenes2[-1].innovationnumber
            lower = 0
        elif tgenes1[-1].innovationnumber >= genes2[-1].innovationnumber:
            #detta ger inte lower eftersom du kommer ha dem i array
            highest = tgenes1[-1].innovationnumber
            lower = tgenes2[-1].innovationnumber
        else:
            highest = tgenes2[-1].innovationnumber
            lower = tgenes1[-1].innovationnumber

        #Anta att du har två arrays
        genes1 = self.createArray(genes1, highest)
        genes2 = self.createArray(genes2, highest)
        disjoint = 0
        excess = 0
        excessState = False
        for i in range(0,highest+ 1): #Ska det vara +1?

            if genes1[i] != genes2[i]:
                if excessState:
                    excess += 1
                    continue
                else:
                    disjoint += 1
            if i == lower: 
                excessState = True
        return disjoint, excess

#Lär finnas något mycket bättre sätt

    def weightDifference(self, genes1, genes2):
        count = 0
        total = 0
        tgenes1 = self.orderGenes(genes1.values())
        tgenes2 = self.orderGenes(genes1.values())
        lower = 0
        if len(tgenes1) == 0 or len(tgenes2) == 0: #går kanske att lägga ovanför?
                return 0
        if tgenes1[-1].innovationnumber >= tgenes2[-1].innovationnumber:
            #detta ger inte lower eftersom du kommer ha dem i array
            lower = tgenes2[-1].innovationnumber
        else:
            lower = tgenes1[-1].innovationnumber
        #Anta att du har två arrays
        genes1 = self.createArray(genes1, lower)
        genes2 = self.createArray(genes2, lower)
        for i in range(0, lower + 1):
            if genes1[i] == genes2[i] and genes1[i] != 0:
                count += 1
                diff = abs(genes1[i] - genes2[i])
                total += diff
        if count == 0: #Vad ska det bli om inga matchar? divide by zero
            return None
        return total/count

    #Kollar ifall genome är kompatibel till den arten
    def isCompatiable(self, testGenome):
        sGenome = self.best.brain
        disjoint, excess = self.findDisjoinGenes(sGenome.connections, testGenome.connections)
        weightDiff = self.weightDifference(sGenome.connections, testGenome.connections) #Spelar ordningen roll?
        threshold = 0.6
        disjointCoefficent = 2
        excessCoefficent = 2
        weightDiffCoefficent = 1
        factorN = 1
        if len(sGenome.connections) < 20 and len(testGenome.connections) < 20:
            factorN = 1 #the factor N, the number of genes in the larger genome, normalizes for genome size (N can be set to 1 if both genomes are small, i.e., consist of fewer than 20 genes). 
        else: 
            factorN = "Lös det här"
        Delta = ((excessCoefficent * excess)/factorN) + ((disjointCoefficent * disjoint)/factorN) + weightDiffCoefficent * weightDiff #Formel för att veta combatiblity från stanley papper
        return Delta < threshold #DET SKA VARA Self.THRESHOLD ELLER NGT HÄR
    
    def tworandomIndivids(self):
        if len(self.individer) == 1: #Ifall det bara finns en indvid i arten får den inviden fortplanta med sig själv...
            return self.best, self.best
        n1, n2 = numpy.random.choice(self.individer, 2)
        if n2.fitness > n1.fitness:
            temp = n2
            n2 = n1
            n1 = temp        
        return n1, n2

    def createChild(self, history):
        #Genome1 ska ha högre eller lika med fitness med genome2
        #KODEN UNDER ANVÄNDS FLERA GÅNGER OCH GÅR ANTAGLIGEN ATT GÖRA OM TILL EN FUNKTION
        genome1, genome2 = self.tworandomIndivids() #Tar två random grabbar
        genome1 = genome1.brain #tar deras hjärnor
        genome2 = genome2.brain
        genes1 = self.orderGenes(genome1.connections.values()) #Ordnar deras geneer
        genes2 = self.orderGenes(genome2.connections.values())
        highest = 0
        #Behöver man ens ordra gensen? räcker det inte med len(genome1.connections)
        if len(genes1) == 0 and len(genes2) == 0:
            babyGenome = genome()
            babyGenome.initalizeNetwork()
            babyGenome.mutate(history)
            baby = player(babyGenome)
            return baby
        elif len(genes1) == 0:
            babyGenome = genome()
            babyGenome.connections = genome2.connections
            babyGenome.nodes = genome2.nodes
            babyGenome.nextnode = genome2.nextnode
            babyGenome.mutate(history)
            baby = player(babyGenome)
            return baby
        elif len(genes2) == 0:
            babyGenome = genome()
            babyGenome.connections = genome1.connections
            babyGenome.nodes = genome1.nodes
            babyGenome.nextnode = genome1.nextnode
            babyGenome.mutate(history)
            baby = player(babyGenome)
            return baby
        
        if genes1[-1].innovationnumber >= genes2[-1].innovationnumber:
            #detta ger inte lower eftersom du kommer ha dem i array
            highest = genes1[-1].innovationnumber
        else:
            highest = genes2[-1].innovationnumber
        #Anta att du har två arrays
        #genes1 = self.createArray(genes1, highest)
        #genes2 = self.createArray(genes2, highest)
        babyGenes = {}
        for innonr in genome1.connections:
            #Ska du bara ta random vikt från föräldrer om det matchar?
            connection = genome1.connections[innonr]
            if genome2.connections[innonr] != None: #Betyder att det matchar
                randomnr = random.choice([0, 1])
                #ta randomly någons vikt.
                if randomnr == 0:
                    #ta från genome1
                    babyGenes[innonr] = connection
                else:
                    babyGenes[innonr] = genome2.connections[innonr]
            else:
                #Behåll alla genes från genome1
                babyGenes[innonr] = connection
            #Alla nodes från genome1 ges bara till barnet
            babyGenome = genome()
            babyGenome.connections = babyGenes
            babyGenome.nodes = genome1.nodes
            babyGenome.nextnode = genome1.nextnode
            babyGenome.layers = genome1.layers
            babyGenome.mutate(history)
            baby = player(babyGenome)
            return baby

    def sharedFitness(self): #Förstår inte riktigt men tror detta gör att inte en art tar över hela populationen
        for individ in self.individer: #Försök göra detta på en radn för jag fattar inte hur man gör (how to run functon on attribute on all objects in list)
            individ.fitness = individ.fitness/len(self.individer)

    def killHalf(self): #Dödar den sämre halvan av arten. Leta efter ett mer systematiskt sätt att döda av arten
        #Problemet med det här är att det kommer döda arter där det finns en kvar
        #https://stackoverflow.com/questions/15715912/remove-the-last-n-elements-of-a-list
        #https://stackoverflow.com/questions/50451570/how-to-divide-a-list-and-delete-half-of-it-in-python
        #Arten måste vara sorterad först
        if len(self.individer) != 1:
            self.individer = self.individer[:len(self.individer)//2]
        

    