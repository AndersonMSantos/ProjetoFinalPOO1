from pessoa import *
class MEDICO(PESSOA):
    def __init__(self, Rua, Num , Comp, Bair, CEP, Cid, Est, Nome, Nasc, Civi, RG, CPF, Gen, Tel, Sang, RH, Esp, Ala):
        PESSOA.__init__(self, Rua, Num , Comp, Bair, CEP, Cid, Est, Nome, Nasc, Civi, RG, CPF, Gen, Tel, Sang, RH)
        self.__especialidade = Esp
        self.__ala = Ala

    def setEspecialidade(self, Esp):
        self.__especialidade = Esp
    def getEspecialidade(self):
        return self.__especialidade

    def setAla(self, Ala):
        self.__ala = Ala
    def getAla(self):
        return self.__ala