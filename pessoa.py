from endereco import *

class PESSOA(ENDERECO):

    def __init__(self, Nome, Nasc, Civi, RG, CPF, Gen, Tel, Sang, RH):
        ENDERECO.__init__(self, Rua, Num , Comp, Bair, CEP, Cid, Est)
        self.__nome = Nome
        self.__dataNas = Nasc
        self.__estCiv = Civi
        self.__rg = RG
        self.__cpf = CPF
        self.__genero = Gen
        self.__telefone = Tel
        self.__sangue = Sang
        self.__rh = RH

    def setNome(self, Nome):
        self.__nome = Nome
    def getNome(self):
        return self.Nome

    def setNascimento(self, Nasc):
        self.__dataNas = Nasc
    def getNascimento(self):
        return self.Nasc

    def setEstadoCivil(self, Civil):
        self.__estCiv = Civil
    def getEstadoCivil(self):
        return self.__estCiv

    def setRG(self, RG):
        self.__rg = RG
    def getRG(self):
        return self.__RG

    def setCPF(self, CPF):
        self.__cpf = CPF
    def get(self):
        return self.__cpf

    def setGenero(self, Gen):
        self.__genero = Gen
    def get(self):
        return self.__genero

    def setTelefone(self, Tel):
        self.__telefone = Tel
    def getTelefone(self):
        return self.__telefone

    def setTipoSangue(self, sang):
        self.__sangue = sang
    def getTipoSangue(self):
        return self.__sangue

    def setRH(self, RH):
        self.__rh = RH
    def getRH(self):
        return self.__rh