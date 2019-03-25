from pessoa import *

class responsavel(PESSOA):

    def __init__(self, Parent):
        PESSOA.__init__(self, Nome, Nasc, Civi, RG, CPF, Gen, Tel, Sang, RH)
        self.__parentesco = Parent

    def setParentesco(self, Parent):
        self.__parentesco = Parent
    def getParentesco(self):
        return self.__parentesco