from pessoa import *
class MEDICO(PESSOA):
    def __init__(self, Esp, Ala):
        PESSOA.__init__(self, Nome, Nasc, Civi, RG, CPF, Gen, Tel)
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