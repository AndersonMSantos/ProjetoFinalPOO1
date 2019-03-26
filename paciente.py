from pessoa import *
from profissao import *
class PACIENTE(PESSOA, PROFISSAO):

    def __init__(self, Rua, Num , Comp, Bair, CEP, Cid, Est, Nome, Nasc, Civi, RG, CPF, Gen, Tel, Sang, RH, Idade, Altura, Peso, IMC, SUS, Priori):
        PESSOA(self, Rua, Num , Comp, Bair, CEP, Cid, Est, Nome, Nasc, Civi, RG, CPF, Gen, Tel, Sang, RH)
        PROFISSAO.__init__(self, RuaE, NumE, CompE, BairE, CEPE, CidE, EstE, TelE, Func)
        self.__idade = Idade #NÃO VAZIO. >= 0. <= 129.
        self.__altura = Altura #>= 0. <= 2,50. NÃO VAZIO
        self.__peso = Peso #>= 0. <= 634. NÃO VAZIO.
        self.__imc = IMC #PESO/ALTURA²
        self.__sus = SUS
        self.__prioridade = Priori #<= 12 = CRIANÇA. >= 65 = IDOSO. > 12 && <65 = UM MERDA QUALQUER.

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

    def setSUS(self, SUS):
        self.__sus = SUS
    def getSUS(self):
        return self.__sus

    def setPrioridade(self, Priori):
        self.__prioridade = Priori
    def getPrioridade(self):
        return self.__prioridade

    """if (Idade <= 10):
        Priori == 1
    elif (Idade >= 65):
        Priori == 2
    else:
        Priori == 3"""
