from endereco import ENDERECOE
class EMPRESA(ENDERECOE):
    """TEL: 8 digitos!
        CEL: 9 digitos! (criar)
    """

    def __init__(self,RuaE, NumE, CompE, BairE, CEPE, CidE, EstE, TelE):
        ENDERECOE.__init__(self, RuaE, NumE, CompE, BairE, CEPE, CidE, EstE)
        self.__TelefoneEmp = TelE

    def setTelefoneEmpresa(self, TelE):
        self.__TelefoneEmp = TelE
    def getTelefoneEmpresa(self):
        return self.__TelefoneEmp