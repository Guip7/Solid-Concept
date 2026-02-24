# Principio de substituição de Liskov

class Animal:
    def comer(self):
        print("O animal está comendo")

    def andar(self):
        print("O animal está andando na jaula")

class Felino(Animal): #Herdou da classe animal
    def lamber(self):
        print("O felino esta se lambendo")
    def comer(self):
        print("O felino está comendo sua comida")

class Leao(Felino):
    def rugir(self):
        print("o leao esta rugindo arrrr")

class Humano:
    def observa(self, animal: Animal): 
        animal.comer()


animal = Animal()
felino = Felino()
leao = Leao()
humano = Humano()


humano.observa(felino) #comportamento não muda
humano.observa(leao)
humano.observa(animal)