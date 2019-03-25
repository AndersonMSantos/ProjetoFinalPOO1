from pessoa import *

class PACIENTE(PESSOA):

    def __init__(self, Idade, Altura, Peso, IMC, Priori):
        PESSOA(self, Nome, Nasc, Civi, RG, CPF, Gen, Tel, Sang, RH)
        self.__idade = Idade
        self.__altura = Altura
        self.__peso = Peso
        self.__imc = IMC
        self.__prioridade = Priori

    def setIdade(self, Idade):
        self.__idade = Idade
    def getIdade(self):
        return self.__idade

    def setAltura(self, Altura):
        self.__altura = Altura
    def getAltura(self):
        return self.__altura

    def setPeso(self, Peso):
        self.__peso = Peso
    def getPeso(self):
        return self.__peso

    def setIMC(self, IMC):
        self.__imc = IMC
    def getIMC(self):
        return self.__imc

    def setPrioridade(self, Priori):
        self.__prioridade = Priori
    def getPrioridade(self):
        return self.__prioridade

    if (Idade <= 10):
        Priori == 1
    elif (Idade >= 65):
        Priori == 2
    else:
        Priori == 3
