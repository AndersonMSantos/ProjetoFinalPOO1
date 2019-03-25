from endereco import *
class EMPRESA(ENDERECO):

    def __init__(self, TelE):
        ENDERECO.__init__(self, Rua, Num, Comp, Bair, CEP, Cid, Est)
        self.__TelefoneEmp = TelE

    def setTelefoneEmpresa(self, TelE):
        self.__TelefoneEmp = TelE
    def getTelefoneEmpresa(self):
        return self.__TelefoneEmp