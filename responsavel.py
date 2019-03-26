from pessoa import *

class responsavel(PESSOA):

    def __init__(self, Rua, Num , Comp, Bair, CEP, Cid, Est, Nome, Nasc, Civi, RG, CPF, Gen, Tel, Sang, RH, Parent):
        PESSOA.__init__(self, Rua, Num , Comp, Bair, CEP, Cid, Est, Nome, Nasc, Civi, RG, CPF, Gen, Tel, Sang, RH)
        self.__parentesco = Parent #NÃO VAZIO.

    def setParentesco(self, Parent):
        self.__parentesco = Parent
    def getParentesco(self):
        return self.__parentesco